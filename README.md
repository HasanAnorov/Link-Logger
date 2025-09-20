# Link-Logger

Link-Logger is a **Python Django REST Framework** backend service that provides secure and efficient
logging of HTTP requests coming from external links.
It is designed to integrate seamlessly with **KanoRAT** (Remote Administration Tool) to deliver real-time
metadata about clicked URLs and connections.

## Key Features

- **Django REST APIs** to handle incoming connections from agent links or URLs.
- **Metadata extraction** from HTTP GET requests (e.g., IP address, user-agent, referrer).
- **Structured log delivery**: forwards important parts of metadata to **KanoRAT**, which then displays the
  information in its logging section.
- **Browser redirection**: when an agent link is clicked, the end-user sees the intended website while
  Link-Logger transparently logs and forwards metadata.
- **Scalable & secure**: built on Django and DRF, supporting modular configuration and production deployment.

## Architecture Overview

```text
[ Agent Link Clicked ]
          |
          v
   Link-Logger Server
          |
   +-------------------------+
   | Extract Metadata        |
   | - IP address            |
   | - User-Agent            |
   | - Referrer / Headers    |
   +-------------------------+
          |
          v
   Forward important data --> KanoRAT Logging Section
          |
          v
   Redirect to example website
```

- **Frontend/Client**: Any browser or device that clicks on the agent link.
- **Backend (this repo)**: Django REST Framework API that processes the request, extracts metadata, and sends logs to KanoRAT.
- **KanoRAT**: Displays and stores the logs for operators.
