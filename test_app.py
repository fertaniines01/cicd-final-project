"""
Tests unitaires basiques pour le projet CI/CD.
Adapte ce fichier au contenu réel de ton app.py si besoin.
"""
import unittest


class TestBasic(unittest.TestCase):
    """Tests de base pour valider que la suite de tests fonctionne."""

    def test_app_module_importable(self):
        """Vérifie que le module principal de l'application peut être importé."""
        try:
            import app  # noqa: F401
        except ImportError:
            self.fail("Impossible d'importer app.py")

    def test_sanity(self):
        """Test de base pour confirmer que nosetests fonctionne."""
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
