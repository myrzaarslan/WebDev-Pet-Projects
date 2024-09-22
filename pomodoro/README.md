# UniCompass - CS50W Capstone Project

## Description

UniCompass is a web application designed to help students in Kazakhstan explore universities in their country. It provides ranking data from two world-renowned university ranking systems: QS (Quacquarelli Symonds) and THE (Times Higher Education). The project also includes a Pomodoro timer feature to assist users with task management and productivity.

## Distinctiveness and Complexity

This project satisfies the distinctiveness and complexity requirements for the following reasons:

1. **Unique Concept**: Unlike previous projects in the course, UniCompass focuses on providing educational information specific to Kazakhstan, combining data from multiple sources and integrating an AI-powered description feature.

2. **Data Integration**: The project fetches and processes data from two different ranking systems (QS and THE) using custom Django management commands, demonstrating the ability to work with external data sources and APIs.

3. **AI Integration**: UniCompass incorporates the Gemini AI API to generate university descriptions, showcasing the integration of advanced AI technologies in web applications.

4. **Advanced Frontend Functionality**: The project utilizes JavaScript to implement features such as instant search, dynamic content loading, and a fully-featured Pomodoro timer with task management capabilities.

5. **Complex Backend**: The backend includes custom Django models, views, and API endpoints to handle university data and user interactions.

6. **Mobile Responsiveness**: The application is designed to be fully responsive, ensuring a seamless experience across different devices.

## Files and Directories

- `unicompass_app/`
  - `models.py`: Contains the `THE_University` and `QS_University` models.
  - `views.py`: Includes views for rendering pages and API endpoints.
  - `urls.py`: Defines URL patterns for the application.
  - `management/commands/fetch_universities.py`: Custom Django command to fetch and update university data.
  - `static/unicompass_app/`
    - `js/ranking_list.js`: Handles the display and interaction with university rankings.
    - `js/pomodoro.js`: Implements the Pomodoro timer and task management features.
  - `templates/unicompass_app/`
    - `index.html`: Main page template.
    - `unipage.html`: Template for individual university pages.
    - `pomodoro.html`: Template for the Pomodoro timer feature.
- `genaicode/`
  - `genai_university.py`: Integrates with the Gemini AI API for university descriptions.
- `requirements.txt`: Lists all Python dependencies.
- `.env`: Contains environment variables (not included in repository).

## How to Run the Application

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables in a `.env` file:
   - `SECRET_KEY`: Django secret key
   - `GOOGLE_API_KEY`: API key for Gemini AI
6. Run migrations: `python manage.py migrate`
7. Fetch university data: `python manage.py fetch_universities`
8. Start the development server: `python manage.py runserver`

## Additional Information

- The project uses custom Django management commands to fetch and update university data periodically.
- The Pomodoro timer feature includes three different timers (Pomodoro, Short Break, Long Break) and a task management system with drag-and-drop functionality.
- University descriptions are generated in real-time using the Gemini AI API when a user visits a university's page.
- The application supports instant search functionality for universities.

## Future Enhancements

- Implement user authentication to allow personalized experiences.
- Add more detailed statistics and comparisons between universities.
- Expand the coverage to include universities from other countries.
- Integrate more productivity tools alongside the Pomodoro timer.