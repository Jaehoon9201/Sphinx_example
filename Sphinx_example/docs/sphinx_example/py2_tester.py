"""
    my solver
    ~~~~~~~~~
"""

class solver_tester(object):
    """두 개의 int 값을 입력받아 다양한 연산을 할 수 있도록 하는 클래스.

    :param int a: a 값
    :param int b: b 값
    """

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def is_same(self):
        """미리 입력받은 a와 b값이 같은지 확인하여 결과를 반환합니다.

        :return: boolean True or False에 대한 결과, a와 b가 값으면 True, 다르면 False

        예제:
            다음과 같이 사용하세요:

            >>> Test(1, 2).is_same()
            False

        """
        return self._a == self._b

    def plus(self):
        """미리 입력받은 a와 b값을 더한 결과를 반환합니다.

        :returns: int a + b에 대한 결과

        예제:
            다음과 같이 사용하세요:

            >>> Test(2, 1).plus()
            3


        """
        return self._a + self._b
