## 1. What is the difference between a readiness and a liveness probe?

- **Readiness Probe:** Checks whether a container is ready to receive traffic. If the probe fails, Kubernetes removes the Pod from the Service endpoints, so it stops receiving requests. The container is not restarted.

- **Liveness Probe:** Checks whether a container is still functioning properly. If the probe fails repeatedly, Kubernetes restarts the container.

**Main difference:** Readiness determines whether a container can receive traffic, while liveness determines whether a container needs to be restarted.

## 2. Why is a Secret not the same as encryption?

A Kubernetes Secret is designed to store sensitive information such as passwords, API keys, and tokens. However, a Secret is not automatically encrypted just because it is called a Secret.

- By default, Kubernetes Secrets are stored in etcd using Base64 encoding, which is not encryption.
- Anyone who can access the Secret or decode its Base64 value can potentially read the original data.
- Encryption at rest must be configured separately to protect Secrets stored in etcd.
- Access should also be restricted using RBAC permissions.

**Main difference:** Base64 is an encoding method (not encryption). Kubernetes Secrets provide a way to manage sensitive data, but additional security measures are needed to protect that data.

## 3. What happens when a container crosses its memory limit?

When a container exceeds its configured memory limit, the Linux kernel may trigger the **OOM (Out Of Memory) Killer**.

- The container's process may be terminated because it exceeded its allowed memory.
- Kubernetes typically reports the container's termination reason as `OOMKilled`.
- Kubernetes may restart the container depending on its restart policy.
- If the container repeatedly exceeds its memory limit, it can enter a `CrashLoopBackOff` state.

**Main difference:** Unlike CPU limits, which generally throttle CPU usage, exceeding a memory limit can cause the container to be terminated.