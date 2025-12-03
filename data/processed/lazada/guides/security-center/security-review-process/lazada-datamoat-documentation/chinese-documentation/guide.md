数据流程图（DFD）说明了系统在输入和输出方面如何处理数据。正如其名称所示，它专注于信息流转，数据来自哪里，去往哪里以及如何存储。

所有数据流图都包括四个主要元素：实体，处理过程，数据存储和数据流。

外部实体 - 也称为起点和终点。这些数据流是DFD的输入和输出。它们可以代表另一个系统或子系统。

处理过程 - 更改或转换数据的活动。它们将传入数据转换为传出数据，因此所有的处理过程必须在DFD上具有输入和输出。

数据存储 - 数据存储不会生成任何操作，只是简单的保存数据以供以后访问。数据存储可以包括长期的保存文件或在等待处理时短存一批文档。

数据流 - 用箭头符号来表示外部实体，处理过程和数据存储之间的数据移动，流的方向。

DFD的示例如下所示：

 ![](https://img.alicdn.com/top/i1/LB1MhMlxhTpK1RjSZFGXXcHqFXa)

请参考下面的DFD说明：

当外部实体触发流程时，它将通过流向的数据存储（信息存储）来搜索/查找详细信息，并提取外部实体视图所需的数据。

外部实体：请参考User

处理过程：请参考"Look up product availability"的执行动作

数据存储：请参考保存数据的"catalog", "product item"和"inventory item"框。

 ![](https://img.alicdn.com/top/i1/LB1ERAnxmzqK1RjSZFHXXb3CpXa)

外部实体：请参考Customer（流程开始和流程结束）。客户下订单时会触发此动作。订单详细信息和货物发票信息将发送到"Process Orders"框。

处理过程：在"Process Orders"框中，"订单和派件"的详细信息被处理并发送到"数据存储 - Orders（数据存储）"

数据存储：请参考"Orders"框，其中存储了所有订单详细信息。

或者：

![](https://img.alicdn.com/top/i1/LB1TUEnxa6qK1RjSZFmXXX0PFXa)