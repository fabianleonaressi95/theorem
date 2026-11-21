#!/usr/bin/env python3
"""Intrinsic angular-defect audit for the ideal truncated icosahedron."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from audit_c60_icosahedral_connection import c60_ideal, reconstruct_faces


def angle(a, b):
    den = np.linalg.norm(a) * np.linalg.norm(b)
    if den < 1e-14:
        raise ValueError('Degenerate edge at vertex.')
    return float(np.arccos(np.clip(np.dot(a, b) / den, -1.0, 1.0)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default='c60_local_angular_defects')
    args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    X, _ = c60_ideal(); faces, _ = reconstruct_faces(X)
    angles_by_vertex = [[] for _ in X]; incident_faces = [[] for _ in X]
    face_records = []
    for fi, face in enumerate(faces):
        aa=[]
        for k,v in enumerate(face):
            prev, nxt = face[(k-1)%len(face)], face[(k+1)%len(face)]
            a=angle(X[prev]-X[v], X[nxt]-X[v])
            angles_by_vertex[v].append(a); incident_faces[v].append(fi); aa.append(a)
        face_records.append({'face':fi,'size':len(face),'angles_rad':aa,'sum_rad':float(sum(aa))})
    edge_set = set()
    for face in faces:
        face = [int(v) for v in face]
        for a, b in zip(face, face[1:] + face[:1]):
            edge_set.add(tuple(sorted((a, b))))
    vertex_records = []; defects = []
    for v,aa in enumerate(angles_by_vertex):
        if len(aa)!=3: raise RuntimeError(f'Vertex {v}: expected 3 incident faces, got {len(aa)}')
        d=2*np.pi-sum(aa); defects.append(d)
        vertex_records.append({'vertex':v,'incident_faces':incident_faces[v],
          'face_sizes':[len(faces[i]) for i in incident_faces[v]],
          'angles_deg':[float(np.degrees(x)) for x in aa],
          'angle_sum_rad':float(sum(aa)),'defect_rad':float(d),'defect_deg':float(np.degrees(d))})
    total=float(sum(defects)); expected=4*np.pi
    report={'topology':{'vertices':len(X),'edges':len(edge_set),'faces':len(faces),
      'pentagons':sum(len(f)==5 for f in faces),'hexagons':sum(len(f)==6 for f in faces),
      'euler_characteristic':len(X)-len(edge_set)+len(faces)},
      'angular_defects':{'count':len(defects),'unique_degrees':sorted(set(round(float(np.degrees(d)),10) for d in defects)),
      'mean_deg':float(np.mean(np.degrees(defects))),'min_deg':float(np.min(np.degrees(defects))),
      'max_deg':float(np.max(np.degrees(defects))),'sum_rad':total,'sum_deg':float(np.degrees(total)),
      'gauss_bonnet_expected_rad':expected,'residual_rad':float(total-expected)},
      'pentagonal_disclination_charge_deg':60,'pentagon_count':12,'pentagon_charge_total_deg':720,
      'interpretation':'The intrinsic 12-degree vertex defect is distinct from the conventional 60-degree pentagonal disclination charge relative to a planar hexagonal lattice.',
      'frank_vector_status':'Not constructed: no canonical vertex normal exists; a vector convention must be explicitly declared.',
      'vertices_detail':vertex_records,'faces_detail':face_records,
      'checks':{'topology_60_90_32':bool(len(X)==60 and len(edge_set)==90 and len(faces)==32),\n      'face_counts_12_pentagons_20_hexagons':bool(sum(len(f)==5 for f in faces)==12 and sum(len(f)==6 for f in faces)==20),\n      'all_vertex_valences_three':all(len(a)==3 for a in angles_by_vertex),
      'all_defects_12deg':bool(np.max(np.abs(np.degrees(defects)-12))<1e-8),
      'gauss_bonnet_4pi':bool(abs(total-expected)<1e-10)}}
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    (out/'report.md').write_text('# C60 intrinsic angular-defect audit\n\n'+
      '- 60 vertices, 90 edges, 32 faces (12 pentagons, 20 hexagons).\n'+
      '- Each vertex has incident angles 108°, 120°, 120° and defect 12°.\n'+
      f'- Total defect: {np.degrees(total):.12g}° = {total:.12g} rad; expected 4π.\n'+
      f'- Gauss–Bonnet residual: {total-expected:.3e} rad.\n'+
      '- 12° intrinsic vertex defect is distinct from the 60° pentagon disclination charge.\n'+
      '- Frank vector not assigned; an explicit axis convention is required.\n')
    print(json.dumps(report['topology'],indent=2)); print(json.dumps(report['angular_defects'],indent=2))
    if not all(report['checks'].values()): raise SystemExit('Audit failed')
if __name__=='__main__': main()
