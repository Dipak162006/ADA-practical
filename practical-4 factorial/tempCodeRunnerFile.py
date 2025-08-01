<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Resume Builder</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>AI-Powered Resume Builder</h1>
        
        <div class="resume-form">
            <div class="form-section">
                <h2>Personal Information</h2>
                <input type="text" id="name" placeholder="Full Name">
                <input type="email" id="email" placeholder="Email">
                <input type="tel" id="phone" placeholder="Phone Number">
            </div>
            
            <div class="form-section">
                <h2>Education</h2>
                <div id="education-fields">
                    <!-- Dynamic fields will be added here -->
                </div>
                <button onclick="addEducationField()">+ Add Education</button>
            </div>
            
            <div class="form-section">
                <h2>Work Experience</h2>
                <div id="experience-fields">
                    <!-- Dynamic fields will be added here -->
                </div>
                <button onclick="addExperienceField()">+ Add Experience</button>
            </div>
            
            <button id="generate-btn" onclick="generateResume()">Generate Resume</button>
        </div>
        
        <div class="resume-preview" id="resume-preview">
            <!-- Generated resume will appear here -->
        </div>
    </div>
    
    <script src="script.js"></script>
</body>
</html>