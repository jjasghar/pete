# PETE
(Patient Engagement Training Experience)

## Scope

This is a helper application for Medical Students to work on their Motiviational Interviewing. The application
helps the Students ask questions and figure out what is wrong with their patient.

## Features

- **Chat Interface**: Interactive chat with AI-generated patients for practicing motivational interviewing
- **Profile Types**: Switch between Adult and Pediatric patient profiles
  - **Adult Profiles**: Patients aged 21-60 with various professional backgrounds
  - **Pediatric Profiles**: Patients aged 2-18 (preschoolers, elementary students, students)
- **New Patient Generation**: Generate new patients with different characteristics
- **Tutor Mode**: Get suggestions and guidance for improving your interviewing skills

## Podman install

1. Have [ollama][ollama] installed.
2. Have [podman-desktop][podman] installed.
   ```bash
   brew install podman-desktop
   ```
3. Have [podman-compose][podmancompose] installed.
   ```bash
   brew install podman-compose
   ```
4. Check out the repository:
   ```bash
   git clone https://github.com/jjasghar/pete
   cd troublesome-patient
   ```
5. Run the `./setup.sh` script. (you only need to do it "once")
6. Start and stop the application with `./start.sh` and `./stop.sh` to your hearts content.

## Manual install

0. Have [ollama][ollama] installed and `granite3.2` installed.
   ```bash
   ollama run granite3.2:latest
   ```

1. Clone the Repo:
   ```bash
   git clone https://github.com/jjasghar/troublesome-patient
   cd troublesome-patient
   ```

2. Set Up Virtual Environment:
   ```bash
   python3 -m venv venv
   source env/bin/activate
   ```

4. Install Dependencies, and migrate the database.
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```

4. Run the Server:
   ```bash
   python manage.py runserver
   ```

Open: Visit <http://localhost:8000/chat/> to start chatting with your pete!

## Future plans

- A way to export/save the conversation.
- Another "app" to take the log and give suggestions on ways to improve the conversation.

## License & Authors

If you would like to see the detailed LICENSE click [here](./LICENSE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2025- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[ollama]: https://ollama.com
[podman]: https://podman-desktop.io
[podmancompose]: https://github.com/containers/podman-compose?tab=readme-ov-file#installation
