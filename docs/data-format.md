# 记录格式

评价记录以 id、work、rubric、criterion、score、revision_reason 表示作品、量表版本、评价目标和修订依据。

记录以 UTF-8 JSON 保存，顶层包含 dataset 和 records。每条记录的 id 在文件中唯一。`fixtures/records.json` 中的例子用于说明输入字段和状态取值。
