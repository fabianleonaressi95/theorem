"""Run a reproducible X6 irrational-rotation / rational-approximant audit."""
import argparse, json
from decimal import Decimal
from pathlib import Path
from models.prism_billiard_coding import approximation_report

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--alpha",default="0.41421356237309504880168872420969807856967187537694")
    p.add_argument("--cf",default="0,2,2,2,2,2,2,2,2")
    p.add_argument("--length",type=int,default=4096)
    p.add_argument("--precision",type=int,default=80)
    p.add_argument("--output",default="prism_billiard_coding.json")
    a=p.parse_args()
    report=approximation_report(Decimal(a.alpha),[int(x.strip()) for x in a.cf.split(",")],a.length,a.precision)
    Path(a.output).write_text(json.dumps(report,indent=2,sort_keys=True)+"\\n",encoding="utf-8")
    print(json.dumps({"output":a.output,"target_frequency_one":report["target_frequency_one"],
      "approximants":[{"p":r["p"],"q":r["q"],"mismatches":r["mismatch_count_vs_decimal_target"]} for r in report["rational_approximants"]]},indent=2))
if __name__=="__main__":
    main()
