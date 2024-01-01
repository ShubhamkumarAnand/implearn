# D-LQ - Dead-Letter Queue

A dead-letter queue (DLQ) is a message queue used to temporarily store messages that a software system cannot process due to errors. When a message fails to be processed, it is sent to the DLQ for further analysis and troubleshooting.

- Developers optimize the maximum retry count to ensure the software performs enough retries before moving messages to the DLQ

- When messages move into the dead-letter queue, developers inspect the erroneous messages to determine the causes. Messages in the DLQ might contain valuable insights to prevent future recurrences of similar issues. After developers analyze and remediate the issues, the system moves the messages out of the DLQ and into the source queue. This allows the sender to continue processing the messages.

- [AWS Article explaining DLQ](https://aws.amazon.com/what-is/dead-letter-queue/)
