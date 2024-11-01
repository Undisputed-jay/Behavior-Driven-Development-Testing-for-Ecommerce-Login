# Behavior-Driven-Testing-for-LoginPage
<h1>Automated Login Testing with Behave and Selenium</h1>

<p>This project automates login functionality testing for a web application using <strong>Behave</strong> and <strong>Selenium WebDriver</strong>, following the behavior-driven development (BDD) approach. The framework tests various login scenarios, such as successful logins, invalid email or password entries, and empty credential submissions, using Selenium WebDriver to interact with the web application. Built with the page object model (POM), the project separates page-specific logic for better maintainability.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#setup-instructions">Setup Instructions</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#folder-structure">Folder Structure</a></li>
    <li><a href="#scenarios-tested">Scenarios Tested</a></li>
    <li><a href="#utility-functions">Utility Functions</a></li>
</ul>

<h2 id="project-overview">Project Overview</h2>
<p>This test suite automates testing for the login functionality of a web application. Each test is written in a BDD style using Behave, and the steps interact with the web application through Selenium. The project utilizes a page object model for maintainable and reusable code.</p>

<h2 id="features">Features</h2>
<ul>
    <li><strong>Login Functionality Testing:</strong> Validates successful and unsuccessful login attempts.</li>
    <li><strong>Page Object Model (POM):</strong> Separates page logic from test logic for readability and maintainability.</li>
    <li><strong>Timestamped Email Generation:</strong> Generates a unique email using a timestamp to test invalid email login attempts.</li>
</ul>

<h2 id="setup-instructions">Setup Instructions</h2>
<ol>
    <li><strong>Clone the Repository</strong>
        <pre><code>git clone &lt;repository-url&gt;
cd &lt;repository-folder&gt;</code></pre>
    </li>
    <li><strong>Install Dependencies</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Set Up WebDriver</strong> Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and add it to your PATH.</li>
</ol>

<h2 id="usage">Usage</h2>
<ol>
    <li><strong>Run Tests</strong>
        <pre><code>behave</code></pre>
    </li>
</ol>

<h2 id="folder-structure">Folder Structure</h2>
<pre><code>
├── features/
│   ├── login.feature           # Contains the login scenarios in Gherkin format
│   └── steps/
│       └── login_steps.py      # Step definitions for the login scenarios
├── pageobject/
│   ├── loginpage.py            # Page object for the login page
│   └── accountpage.py          # Page object for the account page after login
├── utils/
│   └── helper_functions.py     # Utility functions such as email generator
└── README.html                 # Project documentation
</code></pre>

<h2 id="scenarios-tested">Scenarios Tested</h2>
<ol>
    <li><strong>Successful Login:</strong> Validates that the user is redirected to the dashboard after entering valid credentials.</li>
    <li><strong>Login with Invalid Email:</strong> Checks that an appropriate warning is displayed when an invalid email is used.</li>
    <li><strong>Login with Invalid Password:</strong> Verifies that an error message is shown for incorrect passwords.</li>
    <li><strong>Login with Missing Credentials:</strong> Ensures the correct warning is shown when no credentials are submitted.</li>
</ol>

<h2 id="utility-functions">Utility Functions</h2>
<ul>
    <li><strong>generate_email_with_timestamp():</strong> Generates a unique email address for testing invalid email scenarios.</li>
</ul>

<p>This project is designed to make testing the login functionality efficient and scalable, with a focus on ease of maintenance through the page object model.</p>
