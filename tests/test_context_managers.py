from my_advanced_lib.core.context_managers import file_manager


def test_file_manager(tmp_path):
    file = tmp_path / "test.txt"

    with file_manager(file, "w") as f:
        f.write("hello")

    with open(file) as f:
        assert f.read() == "hello"