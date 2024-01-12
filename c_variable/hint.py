from typing import List, Dict, Set, Tuple, Union, Final

# Final 키워드[원하는 자료형] : 변경하지 말자
data: Final[int] = 10
print(data)

class A:
    pass

class B:
    @staticmethod
    def test(data: Union[int, str], number: int | float, data1: A, datas: List[int], data_dict: Dict[str, int]) -> int:
        return 10

