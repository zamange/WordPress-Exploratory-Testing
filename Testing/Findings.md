# Exploratory Testing Report for WordPress

## Date: 
October 21, 2024

## Tester: 
Zamagcina Ngeyane

## Testing Summary
- **Duration of Testing**: 2 hours
- **Scope of Testing**: User registration, post creation, theme customization

## Findings
### User Registration
| Bug ID | Description | Steps to Reproduce | Severity | Status |
|--------|-------------|---------------------|----------|--------|
| 001    | Registration fails with invalid email format | 1. Go to registration page <br> 2. Enter `user@.com` as email and submit | High | Open |
| 002    | Error not displayed for short password | 1. Go to registration page <br> 2. Enter `123` as password and submit | Medium | Open |
| 003    | Username already taken error not clear | 1. Register with an existing username | Medium | Open |

### Post Creation
| Bug ID | Description | Steps to Reproduce | Severity | Status |
|--------|-------------|---------------------|----------|--------|
| 004    | Image not displaying correctly | 1. Create a post with an image | Medium | Open |
| 005    | Video not playing | 1. Create a post with an embedded video | High | Open |

### Theme Customization
| Bug ID | Description | Steps to Reproduce | Severity | Status |
|--------|-------------|---------------------|----------|--------|
| 006    | Theme switch causes layout issues | 1. Change theme to Twenty Twenty-One | High | Open |
| 007    | Customization options not intuitive | 1. Navigate to customize settings | Medium | Open |

### Overall Observations
- The registration process generally works but lacks clarity in error messaging.
- Some posts displayed formatting issues, especially with images.
- Theme customization could be more user-friendly.

## Recommendations
- Improve error messaging for the registration process.
- Investigate image display issues.
- Enhance the user experience in theme customization settings.
