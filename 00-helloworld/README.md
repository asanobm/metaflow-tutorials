# Episode 00-helloworld: Metaflow says Hi!

**This flow is a simple linear workflow that verifies your installation by
printing out 'Metaflow says: Hi!' to the terminal.**

#### Showcasing:
- Basics of Metaflow.
- Step decorator.

#### To play this episode:
1. ```cd metaflow-tutorials```
2. ```python 00-helloworld/helloworld.py show```
3. ```python 00-helloworld/helloworld.py run```


## 실행해 보면
```bash
python 00-helloworld/helloworld.py run 하면 다음과 같은 결과가 출력됩니다.
bash:~/workspace/metaflow$ python 00-helloworld/helloworld.py run
Metaflow 2.12.30 executing HelloFlow for user:asanobm
Validating your flow...
    The graph looks good!
Running pylint...
    Pylint not found, so extra checks are disabled.
2024-11-21 22:58:05.012 Workflow starting (run-id 1732229885012174):
2024-11-21 22:58:05.015 [1732229885012174/**start**/1 (pid 375537)] Task is starting. <<-- 시작한답니다. 갑자기(?)
2024-11-21 22:58:05.099 [1732229885012174/**start**/1 (pid 375537)] HelloFlow is starting. <<-- 이 메시지는 플로우가 시작될 때 출력됩니다.
2024-11-21 22:58:05.114 [1732229885012174/**start**/1 (pid 375537)] Task finished successfully. <<-- 끝났답니다. 응 ?
2024-11-21 22:58:05.116 [1732229885012174/**hello**/2 (pid 375539)] Task is starting. <<-- 시작한답니다. 갑자기(?)
2024-11-21 22:58:05.208 [1732229885012174/**hello**/2 (pid 375539)] Metaflow says: Hi! <<-- hello 메서드에서 처음 출력되는 메시지입니다.
2024-11-21 22:58:05.225 [1732229885012174/**hello**/2 (pid 375539)] Task finished successfully. <<-- 끝났답니다. 응 ?
2024-11-21 22:58:05.226 [1732229885012174/**end**/3 (pid 375541)] Task is starting. <<-- 시작한답니다. 갑자기(?) 멀 시작하는 걸까요 갑자기 ...
2024-11-21 22:58:05.315 [1732229885012174/**end**/3 (pid 375541)] HelloFlow is all done. <<-- end 메서드에서 출력되는 메시지입니다.
2024-11-21 22:58:05.332 [1732229885012174/**end**/3 (pid 375541)] Task finished successfully. <<-- 끝났답니다. 응 ?
```

## 이 튜토리얼에서 배울 수 있는 것

각 스텝마다. `@step` 데코레이터를 사용하여 각 스텝을 정의하고, `@step` 데코레이터의 `next_step` 인자를 사용하여 다음 스텝을 지정합니다. 이 튜토리얼에서는 `HelloFlow`라는 플로우를 정의하고, `start`, `hello`, `end` 세 개의 스텝을 정의합니다. `start` 스텝에서는 플로우가 시작될 때 출력되는 메시지를 출력하고, `hello` 스텝에서는 `Metaflow says: Hi!`라는 메시지를 출력하고, `end` 스텝에서는 플로우가 끝날 때 출력되는 메시지를 출력합니다.

생각보다 딴순해 보임...