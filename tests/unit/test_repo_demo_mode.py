from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


class TestRepoDemoMode(unittest.TestCase):
    def test_problem_statement_present(self) -> None:
        content = (REPO_ROOT / "02-problem-statement.txt").read_text(encoding="utf-8")
        self.assertIn("Top 3 pain points", content)

    def test_readme_mentions_gitops_and_test_modes(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## GitOps (what is real in this repo)", readme)
        self.assertIn("## Test modes (demo vs production)", readme)
        self.assertIn("## License", readme)

    def test_notice_present(self) -> None:
        notice = (REPO_ROOT / "NOTICE.md").read_text(encoding="utf-8")
        self.assertIn("CloudForgeLabs", notice)
        self.assertIn("Freddy D. Alvarez", notice)

    def test_license_is_noncommercial(self) -> None:
        text = (REPO_ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Noncommercial", text)
        self.assertIn("Commercial use requires paid permission", text)

    def test_gitops_validation_script_runs(self) -> None:
        import subprocess
        import sys

        subprocess.run([sys.executable, "scripts/gitops_validate.py"], cwd=str(REPO_ROOT), check=True)

