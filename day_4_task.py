import Day_4_my_module


def main() -> None:
	"""Entry point for this script.

	Keeps the file runnable via the Run button or `python "Day 4 task.py"`.
	Currently this just prints a small header; the imported module already
	prints its own demo output when imported.
	"""
	print("Running Day 4 task:")
	print("rand_int_1_10 ->", Day_4_my_module.rand_int_1_10())
	print("rand_float_0_1 ->", Day_4_my_module.rand_float_0_1())
	print("rand_randrange_1_9 ->", Day_4_my_module.rand_randrange_1_9())
	print("rand_uniform_1_10 ->", Day_4_my_module.rand_uniform_1_10())
	print("heads_or_tails ->", Day_4_my_module.heads_or_tails())
	print("heads_or_tails2 ->", Day_4_my_module.heads_or_tails2())


if __name__ == "__main__":
	main()