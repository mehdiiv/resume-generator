# resume-generator

This Django project provides a user-friendly platform for creating professional CVs with a modern and customizable design. Users can register and provide their personal details, skills, experience, and education, which are then automatically formatted into a visually appealing CV using HTML, CSS, and the SB Admin 2 theme.

Key Features

    User Registration: Users can create accounts by entering their email address, first and last names, and setting a password.
    Profile Management: Users can edit their profiles to update their personal information, including:
        Image (optional)
        LinkedIn and GitHub URLs (optional)
        Phone number (optional)
        City and country
        Short bio about themselves
    Skill Management: Users can add, edit, and remove skills, specifying the category, start and end dates (if applicable), and a brief description.
    Experience Management: Users can add, edit, and remove work experience entries, providing:
        Company name
        Job title
        Category
        Start and end dates
        Description of their responsibilities and achievements
    Education Management: Users can add, edit, and remove educational qualifications, including:
        University name
        Degree earned
        Field of study
        Start and end dates
        Description of their coursework or research
    CV Generation: Based on the provided information, the project automatically generates a well-structured CV in HTML and CSS using the SB Admin 2 theme. This theme offers a clean, professional, and customizable layout.

Technologies Used

    Backend: Django (Python web framework)
    Frontend: HTML, CSS, SB Admin 2 theme (optional)

Customization

    SB Admin 2 Theme:
        Include the SB Admin 2 theme files in your project's static directory.
        Customize the CSS in cv/static/cv/css/style.css (or a similar file) to override the theme's default styles.
    Additional Features:
        Implement user authentication and authorization for enhanced security.
        Integrate with social media platforms like LinkedIn for easier profile data import.
        Allow users to download their CVs in PDF format.

Deployment

    Choose a suitable hosting provider (e.g., Heroku, AWS, Google Cloud).
    Follow the provider's instructions for deploying Django applications.

Conclusion

This Django project provides a solid foundation for building a user-friendly CV creation platform. By following these guidelines, you can customize it to meet your specific requirements and create professional, visually
