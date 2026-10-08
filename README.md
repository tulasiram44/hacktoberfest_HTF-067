# hacktoberfest_HTF-067

# SAHAYA

> SAHAYA is an AI-powered platform that intelligently connects customers with verified cooperative workers through smart matching, demand forecasting, and accessible voice-based services.
## Team

**Team Name:** DARK PROTOCOL


| Member | Contribution   |
| ------ | -------------- |
| Nithin | [Contribution] |
| Pavna Preethikha M | [Contribution] |
| Nehasri Mullapudi | [Contribution] |
| Sattineni V S Tulasi Ram | [Contribution] |


## Problem Statement

### The Problem

India’s informal workforce faces low digital access, high commissions, limited worker verification, and weak access to insurance and welfare, while customers struggle to find reliable skilled workers quickly. SAHAYA addresses this gap by connecting customers with verified cooperative workers through an accessible, AI-enabled platform.

### Why We Chose This Problem

We selected this problem because we saw a real gap between skilled informal workers and customers who need reliable services. We believe solving it can improve access to work, reduce unfair commissions, and help workers get better opportunities and welfare support while making it easier for customers to find trusted workers.

## Solution

SAHAYA is an AI-enabled cooperative workforce platform that connects customers with verified informal workers based on their skills, location, availability, and service requirements.
Customers can describe their requirements naturally, while Gemma 4 helps understand and structure the request into information such as service type, problem, and urgency. The system then uses this information to identify suitable workers.
SAHAYA also aims to make digital services more accessible through voice/IVR-based interaction, allowing workers with limited smartphone or digital access to participate in the platform.
The platform brings together AI-based service understanding, worker matching, federation-based verification, digital payments, and worker welfare support in a single ecosystem.

### Key Features

1. AI-Based Service Understanding
2. Verified Worker Matching
3. IVR Accessibility
4. Worker Welfare Ecosystem

## Innovation and Differentiation

SAHAYA is not designed as a conventional worker marketplace. Instead, it combines AI, cooperative worker networks, accessibility, and welfare support into a single platform.
A major differentiator is that the system does not assume every informal worker has strong digital access. The planned voice/IVR interface allows workers to participate using basic phone access.
The platform also focuses on verified cooperative workers rather than an open marketplace, helping establish trust between customers and workers while supporting a more worker-centric economic model.

## Technical Implementation

### Architecture

[Add the system architecture or workflow Mermaid diagram here.]

### Technology Stack


| Category        | Technologies                |
| --------------- | --------------------------- |
| Frontend        | [Technologies / N/A]        |
| Backend         | [Technologies / N/A]        |
| Database        | [Technologies / N/A]        |
| AI / ML         | [Models / frameworks / N/A] |
| Infrastructure  | [Technologies / N/A]        |
| APIs / Services | [Services / N/A]            |


If a category or technology is not implemented in the project, specify `N/A` instead of leaving the field blank.

### How It Works

1. A customer creates a service request through the SAHAYA application.
2. The customer can describe the requirement using natural language.
3. Gemma 4 processes the request and identifies relevant information such as the required service, problem type, and urgency.
4. The structured request is passed to the worker-matching system.
5. The system considers worker skills, location, availability, and verification status.
6. Suitable workers are ranked and presented to the customer.
7. The customer selects a worker and creates a booking.
8. The booking and service information are stored for future reference.
For workers with limited digital access, the platform can additionally provide a voice/IVR-based interaction mechanism.
### Technical Decisions

We chose a modular architecture so that AI processing, worker matching, authentication, booking, and data management can operate as separate components.
Gemma 4 was selected for natural-language understanding because it allows the application to use an open-weight AI model for processing service requests without depending entirely on proprietary hosted AI APIs.
The AI layer is separated from the matching logic. Gemma converts an unstructured customer request into structured information, while the application logic uses factors such as location, skills, availability, and verification to determine suitable workers.
This separation makes the system easier to test, maintain, and extend.

## Implementation During the Hackathon

[Describe what the team built during the Hack Day and the major functionality or components completed during the event.]

### Team Contributions

- **Nithin:** [Contribution]
- **Pavna Preethikha M:** [Contribution]
- **Nehasri Mullapudi:** [Contribution]
- **Sattineni V S Tulasi Ram:** [Contribution]

## Working Application

**Live Application:** [Live URL]

[Briefly explain how the deployed application can be accessed and what functionality can be tested.]

The submitted application should be functional and accessible through the provided link where applicable.

## Demo Video

**Demo Video:** [Video URL]

[Provide a short demonstration of the working project, covering the main user flow and important functionality.]

## Open Source and AI Usage

### AI / Models

- **[Model]:** [How it is used]

### Open Source Components

- **[Library / Framework]:** [Purpose]
- **[Dataset]:** [Purpose]
- **[API / Service]:** [Purpose]

[Include relevant licenses, attribution, and acknowledgements for external components.]

## Setup and Usage

### Prerequisites

- [Requirement]
- [Requirement]

### Installation

```bash
git clone [repository-url]
cd [project-directory]
[installation-command]
```

### Environment Variables

```env
[VARIABLE_NAME]=[value]
```



### Running the Project

```bash
[run-command]
```

### Usage

[Explain the basic steps required to use the project.]

## Devpost Submission

**Devpost Project:** [Devpost Project URL]

[Add the link to the team's Devpost submission. Ensure the Devpost project page is complete and contains the required project information, links, media, and team details.]

## Credits and License

### Credits

[Credit libraries, frameworks, datasets, models, APIs, contributors, and other external resources used.]

### License

[License name and/or link.]

## Submission Checklist

- [ ] Project title and description added
- [ ] All team members listed
- [ ] Problem clearly explained
- [ ] Reason for choosing the problem explained
- [ ] Solution and key features documented
- [ ] Innovation and differentiation explained
- [ ] Architecture included
- [ ] Technical implementation documented
- [ ] Work completed during the hackathon documented
- [ ] Team contributions documented
- [ ] Working application is functional
- [ ] Live application link added where applicable
- [ ] Demo video added
- [ ] AI and open-source components documented
- [ ] Setup and usage instructions tested
- [ ] Challenges and learnings documented
- [ ] Devpost submission completed
- [ ] Devpost link added
- [ ] Credits added
- [ ] License added
- [ ] Repository is organized and complete

