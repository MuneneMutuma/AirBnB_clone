import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test class for unittests for AirBnB Clone project
    """

    # ------------------------ 3. Base Model --------------------
    def test_init(self):
        base1 = BaseModel()

    def test_id(self):
        base = BaseModel()
        from_base = base.__dict__
        from_dict = base.to_dict()
        self.assertEqual(from_base["id"], from_dict["id"])

    def test_created_at(self):
        base = BaseModel()
        from_base = base.__dict__
        from_dict = base.to_dict()
        self.assertEqual(
                from_base["created_at"].isoformat(),
                from_dict["created_at"])

    def test_updated_at(self):
        base = BaseModel()
        from_base = base.__dict__
        from_dict = base.to_dict()
        self.assertEqual(
                from_base["updated_at"].isoformat(),
                from_dict["updated_at"])

    def test_class_name(self):
        base = BaseModel()
        from_base = base.__dict__
        from_dict = base.to_dict()
        self.assertEqual(base.__class__.__name__, from_dict["__class__"])

    # -------- 4. Create BaseModel from Dictionary Tests -------
    def test_no_kwargs(self):
        base = BaseModel()
        self.assertTrue(base.__class__.__name__ == 'BaseModel')

    def test_kwargs_id(self):
        base = BaseModel()
        base_dict = base.to_dict()

        from_dict = BaseModel(**base_dict)
        self.assertEqual(base.id, from_dict.id)

    def test_kwargs_created_at(self):
        base = BaseModel()
        base_dict = base.to_dict()

        from_dict = BaseModel(**base_dict)

        self.assertEqual(base.created_at, from_dict.created_at)

    def test_kwargs_updated_at(self):
        base = BaseModel()
        base_dict = base.to_dict()

        from_dict = BaseModel(**base_dict)

        self.assertEqual(base.updated_at, from_dict.updated_at)


if __name__ == "__main__":
    unittest.main()
