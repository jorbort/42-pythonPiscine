from ft_filter import ft_filter
import sys

def main() :
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        if sys.argv[2].isdigit() != True:
            raise AssertionError("AssertionError: the arguments are bad")
        lst = sys.argv[1].split(" ")
        num = int(sys.argv[2])
        filtered_list = ft_filter(lambda x: len(x) >= num , lst)
        print(filtered_list)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
	main()