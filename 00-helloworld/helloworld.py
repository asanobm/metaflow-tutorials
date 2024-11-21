from metaflow import FlowSpec, step


class HelloFlow(FlowSpec):
    """
    Metaflow가 'Hi'를 출력하는 플로우입니다.

    Metaflow가 올바르게 설치되었는지 확인하려면 이 플로우를 실행하세요.

    """

    @step
    def start(self):
        """
        이것은 'start' 단계입니다. 모든 플로우는 플로우의 첫 번째 단계인 'start'라는 단계를 가져야 합니다.

        """
        print("HelloFlow is starting.") # 이 메시지는 플로우가 시작될 때 출력됩니다.
        self.next(self.hello) # 'start' 단계가 완료되면 'hello' 단계로 이동합니다.

    @step
    def hello(self):
        """
        Metaflow가 자신을 소개하는 단계입니다.

        """
        print("Metaflow says: Hi!")
        self.next(self.end)

    @step
    def end(self):
        """
        이것은 'end' 단계입니다. 모든 플로우는 플로우의 마지막 단계인 'end' 단계를 가져야 합니다.

        """
        print("HelloFlow is all done.")


if __name__ == "__main__":
    HelloFlow()
