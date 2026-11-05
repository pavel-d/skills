"""Protect existing user instructions while updating the managed activation rule."""

import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    "configure_babysit", Path(__file__).with_name("configure-babysit.py")
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ManagedPolicyTests(unittest.TestCase):
    def test_preserves_unrelated_guidance_and_is_idempotent(self):
        original = "# Existing policy\n\nKeep this byte for byte.\n"
        updated = MODULE.with_policy(original, "New policy\n")
        self.assertTrue(updated.startswith(original))
        self.assertEqual(MODULE.with_policy(updated, "New policy\n"), updated)

    def test_updates_only_managed_block(self):
        original = f"Before\n{MODULE.BEGIN}\nOld\n{MODULE.END}\nAfter\n"
        updated = MODULE.with_policy(original, "New")
        self.assertEqual(
            updated,
            f"Before\n{MODULE.BEGIN}\n\nNew\n\n{MODULE.END}\nAfter\n",
        )

    def test_rejects_damaged_duplicate_or_reversed_markers(self):
        for content in (
            MODULE.BEGIN,
            MODULE.END,
            MODULE.BEGIN + MODULE.BEGIN + MODULE.END,
            MODULE.END + MODULE.BEGIN,
        ):
            with self.subTest(content=content), self.assertRaises(ValueError):
                MODULE.with_policy(content, "New")


if __name__ == "__main__":
    unittest.main()
