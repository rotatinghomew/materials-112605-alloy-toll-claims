# 委托熔炼交换

重量均为克。保底合同用最低金属重量判断欠补。每一等级先按保底合同中实际承诺的等级保留可满足的金属量。保底客户之间按投料确认时刻办理，同刻比较合同号。未被占用的产出按验收份额客户的已确认净投入比例分摊，限制等级的合同只能实际取得认可的等级，因限制少领的部分保留差额待核。牌号和可替代等级由合同注明。化验单的等级按炉次阈值及报告覆盖的出炉段确认，尚未出化验的出炉段不得用于最终提货。补足承诺与原处置凭证各有身份。可转让数量不含已称出或正等待交提凭证的量。

资料使用 UTF-8 JSON。每个集合各自维护记录 id，跨集合引用使用相应记录 id。事件中的 happened 是业务发生时间，arrived 是对接方可提供该回执的时间。到达时间不能代替业务时间。这些记录来自不同流程阶段，读到一个回执并不代表本地已做过相应操作。

## `owners`

客户认可的提货等级与自用/补足安排。字段为 `id`, `principal`, `mode`, `minimum`, `grades`, `cross_heat`。

## `heats`

配炉输入牌号、产出等级阈值和开炉时间。字段为 `id`, `alloy`, `max_feed`, `threshold_h`, `threshold_m`, `started`。

## `feed`

寄存方可能与货主不同。pure 为交接认可净金属量。字段为 `id`, `alloy`, `depositor`, `owner`, `mass`, `pure`, `assigned`, `consent`, `delivered`。

## `taps`

实物出炉段和称重。字段为 `id`, `heat`, `mass`, `happened`。

## `assay`

化验以 purity 百分比区分等级，phase 描述暂定或签定。字段为 `id`, `tap`, `purity`, `phase`, `replaces`, `happened`。

## `claims`

可办理的提货和所有权转让请求。字段为 `id`, `owner`, `recipient`, `heat`, `grades`, `qty`, `operation`, `happened`。

## `receipts`

交提点过磅可分多次；量对应本条回执。字段为 `id`, `claim`, `stage`, `qty`, `happened`, `arrived`。

## 回执查询

本机回放只提供对接方的既有回执。`GET /v1/receipts?at=...` 的 `at` 是 URL 编码后的带偏移时间，返回对象中 `receipts` 是在该时间之前及当时可取得的回执。同一条数据可以在连续查询中出现，列表先后不代表业务先后。`503` 表示当前无法查询回执。
