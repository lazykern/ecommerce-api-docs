A data flow diagram (DFD) illustrates how data is processed by a system in terms of inputs and outputs. As its name indicates, its focus on the flow of information, where data comes from, where it goes and how it gets stored.

All data flow diagrams include four main elements: entity, process, data store and data flow.

**External Entity** – Also known sources (start point) and terminators (End point). These data flows are the inputs and outputs of the DFD. They can represent another system or indicate a subsystem.

**Process** – An activity that changes or transforms data. Since they transform incoming data to outgoing data, all processes must have inputs and outputs on a DFD.

**Data Store** – A data store does not generate any operations but simply holds data for later access. Data stores could consist of files held long term or a batch of documents stored briefly while they wait to be processed.

**Data Flow** – Movement of data between external entities, processes and data stores is represented with an arrow symbol, which indicates the direction of flow. 

Sample DFD as shown below:

![](https://img.alicdn.com/top/i1/LB1ybr5qxWYBuNjy1zkXXXGGpXa)

Please refer below for the description of the DFD:

When an **external entity** triggers the **process,** it will search/look up for the details by flowing to **data store (information store)** and extract the needed data for the external entity view.

**External entity** : Refer to the User

**Process:** Refer to the activity perform which is “Look up product availability”

**Data store:** Refer to the “catalog, product item & inventory item” box where the data is kept.

![](https://img.alicdn.com/top/i1/LB13CLvqAyWBuNjy0FpXXassXXa)

**External entity** : Refer to the customer (at the beginning of the flow and end of the flow). This action trigger when Customer make an order. The order details and goods invoice will be flown to Process order box.

**Process:** In “Process order” box, “get order & goods dispatch” details being process and flown to “data store – Orders (storing information)”

**Data store:** Refer to the “orders” box whereby all the order details are stored in.

OR

![](https://img.alicdn.com/top/i1/LB10vJlqTJYBeNjy1zeXXahzVXa)