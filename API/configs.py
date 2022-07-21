ENDPOINT_ID="6439540536721276928"
PROJECT_ID="gcp-01-356703"

eg_body = """
Containers have shifted the way we think about virtualization. You may remember the days (or you may still be living them) when a virtual machine was the full stack, from virtualized BIOS, operating system, and kernel up to each virtualized network interface controller (NIC). You logged into the virtual box just as you would your own workstation. It was a very direct and simple analogy.

And then containers came along, starting with LXC and culminating in the Open Container Initiative (OCI), and that's when things got complicated.

Idempotency
In the world of containers, the "virtual machine" is only mostly virtual. Everything that doesn't need to be virtualized is borrowed from the host machine. Furthermore, the container itself is usually meant to be ephemeral and idempotent, so it stores no persistent data, and its state is defined by configuration files on the host machine.

If you're used to the old ways of virtual machines, then you naturally expect to log into a virtual machine in order to interact with it. But containers are ephemeral, so anything you do in a container is forgotten, by design, should the container need to be restarted or respawned.

The commands controlling your container infrastructure (such as oc, crictl, lxc, and docker) provide an interface to run important commands to restart services, view logs, confirm the existence and permissions modes of an important file, and so on. You should use the tools provided by your container infrastructure to interact with your application, or else edit configuration files and relaunch. That's what containers are designed to do.

Linux Containers

What are Linux containers?
An introduction to container terminology
Download: Containers Primer
Kubernetes Operators: Automating the container orchestration platform
eBook: Kubernetes patterns for designing cloud-native apps
What is Kubernetes?
For instance, the open source forum software Discourse is officially distributed as a container image. The Discourse software is stateless, so its installation is self-contained within /var/discourse. As long as you have a backup of /var/discourse, you can always restore the forum by relaunching the container. The container holds no persistent data, and its configuration file is /var/discourse/containers/app.yml.

Were you to log into the container and edit any of the files it contains, all changes would be lost if the container had to be restarted.

LXC containers you're building from scratch are more flexible, with configuration files (in a location defined by you) passed to the container when you launch it.

A build system like Jenkins usually has a default configuration file, such as jenkins.yaml, providing instructions for a base container image that exists only to build and run tests on source code. After the builds are done, the container goes away.

Now that you know you don't need SSH to interact with your containers, here's an overview of what tools are available (and some notes about using SSH in spite of all the fancy tools that make it redundant).

OpenShift web console
OpenShift 4 offers an open source toolchain for container creation and maintenance, including an interactive web console.

When you log into your web console, navigate to your project overview and click the Applications tab for a list of pods. Select a (running) pod to open the application's Details panel.

Pod details in OpenShift
opensource.com

Click the Terminal tab at the top of the Details panel to open an interactive shell in your container.

A terminal in a running container
opensource.com

If you prefer a browser-based experience for Kubernetes management, you can learn more through interactive lessons available at learn.openshift.com.

OpenShift oc
If you prefer a command-line interface experience, you can use the oc command to interact with containers from the terminal.

First, get a list of running pods (or refer to the web console for a list of active pods). To get that list, enter:

$ oc get pods
You can view the logs of a resource (a pod, build, or container). By default, oc logs returns the logs from the first container in the pod you specify. To select a single container, add the --container option:

$ oc logs --follow=true example-1-e1337 --container app


"""

eg_title = "Google Home enables users to speak voice commands to interact with services through the Home's intelligent personal assistant called Google Assistant. A large number of services, both in-house and third-party, are integrated, allowing users to listen to music, look at videos or photos, or receive news updates entirely by voice. "
