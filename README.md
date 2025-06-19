# PETE
(Patient Engagement Training Experience)

## Overview

PETE is a Django web application designed to help medical students and healthcare professionals practice **Motivational Interviewing** skills through AI-powered patient interactions. The application provides a safe, controlled environment for learning and improving communication techniques with virtual patients.

## Features

### Chat Interface (`/chat/`)
- **Interactive AI Patients**: Chat with AI-generated patients powered by Ollama (Granite 3.2 model)
- **Realistic Patient Profiles**: Choose from adult (ages 21-60) or pediatric (ages 2-18) patient scenarios
- **Dynamic Patient Generation**: Each session creates a unique patient with varying:
  - Health conditions (minor, major, critical)
  - Attitudes toward treatment (low, medium, high intensity)
  - Emotional states (low, medium, high spirits)
  - Professional backgrounds or age-appropriate descriptions
- **Conversation Logging**: All interactions are automatically saved for later review
- **Markdown Formatting**: Responses are formatted for improved readability

### Tutor/Suggestions Interface (`/suggestions/`)
- **MITI-Based Feedback**: Get coaching based on Motivational Interviewing Treatment Integrity (MITI) criteria
- **Conversation Analysis**: Upload previous chat logs (.log, .txt files) for detailed feedback
- **Performance Improvement**: Receive specific suggestions for enhancing interviewing techniques
- **Rubric Scoring**: Get MITI rubric evaluations of your conversations

### Patient Profile Types
- **Adult Profiles**: Professional adults with various health challenges including:
  - Substance use concerns (caffeine, alcohol, nicotine)
  - Chronic conditions (diabetes, hypertension)
  - Lifestyle-related issues (diet, exercise, sleep)
  - Preventive care scenarios
- **Pediatric Profiles**: Age-appropriate scenarios for children including:
  - Screen time and sleep issues
  - Physical activity and nutrition
  - Age-specific behavioral concerns

## Installation

### Option 1: Containerized Deployment (Recommended)

**Prerequisites:**
- [Ollama](https://ollama.com) installed
- [Podman Desktop](https://podman-desktop.io) or Docker installed
- [Podman Compose](https://github.com/containers/podman-compose) installed

```bash
# Install podman-desktop and podman-compose (macOS)
brew install podman-desktop podman-compose

# Clone the repository
git clone https://github.com/jjasghar/pete
cd pete

# Run setup (one-time only)
./setup.sh

# Start the application
./start.sh

# Stop the application
./stop.sh
```

### Option 2: Manual Installation

**Prerequisites:**
- Python 3.8+
- [Ollama](https://ollama.com) with Granite 3.2 model

```bash
# Install and run Ollama with Granite 3.2
ollama run granite3.2:latest

# Clone the repository
git clone https://github.com/jjasghar/pete
cd pete

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## Usage

1. **Access the Application**: Visit `http://localhost:8000`
2. **Practice Interviews**: Go to `/chat/` to start practicing with AI patients
3. **Switch Profile Types**: Use the interface to toggle between adult and pediatric patients
4. **Generate New Patients**: Reload to get a new patient with different characteristics
5. **Get Feedback**: Visit `/suggestions/` to upload conversation logs and receive MITI-based coaching
6. **Review Conversations**: Check the `previous_chats/` directory for saved conversation logs

## Technical Details

- **Backend**: Django 5.2 with SQLite database
- **AI Model**: Granite 3.2 via Ollama
- **Patient Data**: CSV-based profile system with realistic scenarios
- **Logging**: Automatic conversation logging with timestamps
- **File Processing**: Support for .log and .txt file uploads for analysis
- **Containerization**: Multi-service setup with Ollama and web application containers

## Configuration

- **Ollama Host**: Set `OLLAMA_SELF_HOST` environment variable for custom Ollama instances
- **Patient Profiles**: Modify CSV files in `/profiles/` to customize patient scenarios
- **Logging**: Conversations are saved in `/previous_chats/` directory

## Future Enhancements

- Enhanced conversation export capabilities
- Additional patient profile categories
- Expanded MITI rubric integration
- Progress tracking and analytics
- Multi-user support with authentication

## License & Authors

Licensed under the Apache License, Version 2.0. See [LICENSE](./LICENSE) for details.

**Author**: JJ Asghar <awesome@ibm.com>

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

---

**About MITI**: The Motivational Interviewing Treatment Integrity (MITI) is a standardized coding system used to evaluate the quality and fidelity of motivational interviewing sessions. It helps practitioners improve their skills through structured feedback and assessment.
