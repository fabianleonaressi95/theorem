"""Exact incidence-count check for the proposed RC-to-snub-cube face split."""

def test_twelve_square_faces_split_match_snub_cube_counts():
    # Rhombic cuboctahedron endpoint, as reconstructed in T154.
    vertices, edges = 24, 48
    triangles, squares = 8, 18

    split_squares = 12
    triangles_after = triangles + 2 * split_squares
    squares_after = squares - split_squares
    edges_after = edges + split_squares
    faces_after = triangles_after + squares_after

    assert (vertices, edges_after, faces_after) == (24, 60, 38)
    assert (triangles_after, squares_after) == (32, 6)
    assert vertices - edges_after + faces_after == 2
