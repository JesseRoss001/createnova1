# Welcome to Create Nova

Create Nova is your one-stop solution for all your digital marketing and web development needs in Indonesia. We are dedicated to providing top-notch services to small and medium-sized businesses, offering cost-effective solutions to boost your online presence and brand recognition.

Whether you're looking to collaborate with content creators, supercharge your brand's advertising efforts, develop a stunning website, or need bespoke web design services, Create Nova has you covered. Our team of experts is committed to helping you achieve your business goals efficiently and affordably.

In this README, you'll find all the essential information you need to get started with Create Nova, including our services, pricing, and how to get in touch with us. Let's embark on a journey to elevate your brand and expand your digital footprint together!

---

## User Types in Create Nova

Create Nova, hosted on Heroku and utilizing ElephantSQL, offers a diverse range of functionalities catered to different user types. Each user type has access to various features and tools within our platform, ensuring a customized experience that aligns with their specific needs and goals. Here are the four main types of users on Create Nova:

### 1. **Administrators**
As the backbone of Create Nova, administrators have full access to the system. They manage user accounts, oversee site content, ensure the smooth operation of all services, analyze data, generate reports, and maintain the overall health of the platform.

### 2. **Content Creators**
These users are the creative force behind the digital content on our platform. Content creators can design, upload, and manage their digital works. They collaborate with brands, receive feedback, and track the performance of their content.

### 3. **Staff Members**
Staff members are crucial in supporting both the operational and strategic aspects of Create Nova. They assist in managing the platform, provide support to other user types, and help in executing digital marketing and web development projects.

### 4. **Businesses**
Business clients use Create Nova to enhance their online presence and branding efforts. They have access to a range of digital marketing tools, web design services, and can collaborate with content creators. They can manage campaigns, analyze performance, and utilize creative professionals' services.

---

Each user type is integral to the ecosystem of Create Nova, contributing uniquely to the growth and success of digital marketing and web development ventures in Indonesia. Our platform is designed to be intuitive and user-friendly, ensuring a seamless experience for all.

If you're interested in learning more about how Create Nova can help your business, visit our website at [createnova.org](http://createnova.org) or get in touch with our team for personalized assistance.

## Technology Stack

Create Nova is built using a robust and scalable technology stack, ensuring high performance, security, and ease of use. Our choice of technologies reflects our commitment to delivering top-quality services. Here's an overview of the primary technologies used in Create Nova:

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design. It's known for its simplicity and flexibility.
- **Python**: As our core programming language, Python offers readability, efficiency, and a vast ecosystem of libraries and tools.
- **ElephantSQL**: An SQL database service that provides managed PostgreSQL databases. ElephantSQL offers automated backups, data encryption, and scalability.
- **Heroku**: A cloud platform as a service (PaaS) supporting several programming languages. Heroku is used for deploying, managing, and scaling modern apps.

These technologies were chosen for their reliability, ease of integration, and support for agile development practices.

---

## Preliminary Models for User Types

Below are the basic Django models representing the four main types of users in Create Nova. These models are preliminary and may be refined as the development progresses.

### 1. Administrator Model

```python
from django.db import models

class Administrator(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=True)

    def __str__(self):
        return self.username
```
### 2. Creator Model
```python
class ContentCreator(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    portfolio_url = models.URLField(blank=True)

    def __str__(self):
        return self.username
```
### 3. Staff Model
```python
class StaffMember(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.username
```
### 4. Business  Model
```python
class Business(models.Model):
    business_name = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name
````
As an Administrator, I want to generate and disable pins for new staff so that I can manage staff access to the platform.

As an Administrator, I want to view details of all staff and content creators to monitor platform activity and user engagement.

As an Administrator, I want to calculate and monitor staff payments to ensure timely and accurate compensation.

As a Staff Member, I want to generate tokens for new content creator profiles to facilitate their onboarding process.

As a Staff Member, I want to update and manage the gallery with content from creators to showcase their work effectively.

As a Staff Member, I want to upload documents and reports to maintain a record of our business operations.

As a Staff Member, I want to input business contacts and mark their interest levels to track potential client engagement.

As a Managerial Staff Member, I want to access weekly staff reports to oversee staff performance and project progress.

As a Managerial Staff Member, I want to manage meeting schedules via a calendar to ensure efficient time management.

As a C-Level Executive, I want comprehensive access to all platform functionalities to oversee the entire operation.

As a C-Level Executive, I want to access detailed project progress reports to make informed strategic decisions.

As a Content Creator, I want to display my portfolio on the platform to attract potential business collaborations.

As a Content Creator, I want to list my areas of expertise to match with relevant business opportunities.

As a Content Creator, I want to link my social media profiles to increase my online presence and reach.

As a Content Creator, I want to set a provisional price list to inform businesses about my service rates.

As a Business Client, I want to view different service packages to choose the one that best suits my needs.

As a Business Client, I want to read testimonials to gauge the credibility and quality of Create Nova's services.

As a Website Visitor, I want to easily navigate through the Home, About Us, and Contact pages for a seamless experience.

As a Developer, I want to implement SEO strategies to increase the website's visibility and attract more users.

As a Developer, I want to optimize website speed to ensure a fast and responsive user experience.

## Pages Overview

Create Nova features several key pages, each designed to cater to the different needs of our users:

### Home Page
- A welcoming interface showcasing our services and unique value propositions.

### For Businesses
- Dedicated section for business clients, detailing services, packages, and collaboration opportunities.

### For Creators
- A space for content creators to explore opportunities, showcase their work, and connect with businesses.

### For Staff
- Information and tools for staff members to manage their tasks and access essential resources.

### Contact Details
- Comprehensive contact information for Create Nova, including email, phone, and physical address.

### Gallery
- A curated collection of work samples from our accomplished content creators.

### Packages
- Detailed information on the various service packages we offer, tailored to different client needs.

### About Us
- Insight into Create Nova's mission, vision, and the team behind our success.

### Testimonials
- Real-world feedback and endorsements from our satisfied clients and partners.

---

## Business View

### Types of Users in Create Nova

#### Admin
- Can generate and disable pins for new staff.
- View details of all staff and content creators.
- Monitor and calculate staff payments (weekly/monthly).

#### Staff
- Generate tokens for new content creator profiles.
- Manage and update the gallery with content from creators.
- Upload proof documents and daily reports.
- Input business contacts and mark their interest levels.
- Update successful business interactions and related reports.
- **Managerial Level**
  - Access weekly staff reports and project progress.
  - Manage meeting schedules via a calendar.
- **C-Level**
  - Comprehensive access to all platform functionalities.
  - Detailed project progress reports and calendar management.

#### Content Creator Profile
- Display number of creators in our agency.
- Portfolio links and area of expertise.
- Social media links and provisional price lists.
- Showcases including website fees, packages, and client lists.

---

## Optimization and SEO Strategies

To ensure the best user experience and high visibility:

- **Speed Optimization**: Implementing techniques for a fast-loading website.
- **SEO-Friendly Content**: Including relevant keywords throughout the site.
- **Regular Updates**: Ensuring the website remains up-to-date and ranks higher in search results.

---
