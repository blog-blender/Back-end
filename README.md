# Blog Blender

Social Media Platform Backend Server
[deployed server](https://back-8zqrewq3a-blog-blender.vercel.app/api/v1/accounts/register)
## table of end points:
| No. | Name                                    | Path                                                     | Input                                       | Output                            |
| --- | --------------------------------------- | -------------------------------------------------------- | ------------------------------------------- | --------------------------------- |
| ----|  GET METHODS  |   --------------------------     |     -------------------------   |     -----------------------------------------------   |
| 1   | Specific Blog Posts                    | `http://127.0.0.1:8001/api/v1/posts/?blog_id=[blog_id]` | Blog ID, Number of Posts                  | List of Posts Sorted by Date     |
| 2   | List of All Followed Blogs              | `http://127.0.0.1:8000/api/v1/blogs/userfollowing/?[user_id]` | User ID                                    | List of Followed Blogs           |
| 3   | List of All Owned Blogs                 | `http://127.0.0.1:8000/api/v1/blogs/?[owner]`            | User ID                                    | List of Owned Blogs              |
| 4   | Post Detail                             | `http://127.0.0.1:8000/api/v1/posts/details/?[post_id]` | Post ID                                    | Post Title, Content, Photos, Comments, Likes |
| 5   | Random Posts from Blog                 | `http://127.0.0.1:8000/api/v1/posts/home/?[user_id=2]&[num_of_posts=1]` | Blog ID (User ID), Posts Number          | List of Posts                     |
| 6   | Search Blog                             | `http://127.0.0.1:8000/api/v1/blogs/search/?[category=gym]&[blog_title=cooking]` | Blog Name (Optional if Filters Provided), Number of Blogs, Filters (Optional) | List of Blogs Ordered by Similarity to Blog Name |
| 7   | Get All Categories                     | `http://127.0.0.1:8000/api/v1/blogs/categories/`         | Empty                                       | List of All Categories           |
| 8   | Get User Detail                        | `http://127.0.0.1:8000/api/v1/accounts/users?username=[eman]` | User Name                                  | User Name, First Name, Last Name, Profile Photo, Email |
| 9   | Get Blog Details                       | `http://127.0.0.1:8000/api/v1/blogs/[blog_id]/`         | -                                           | -                                 |
| 10  | Get Most Recent Posts (My Own Posts)  | `http://127.0.0.1:8000/api/v1/posts/recent/?user_id=1&num_of_posts=4` | User ID, Number of Posts                 | List of Recent Posts             |
| 11  | List of User Followers                 | `http://127.0.0.1:8000/api/v1/blogs/user_friends/?user_id=1` | User ID                                    | List of Users Following Blogs by User ID |
| ------  |      CREATE METHODS        |      ---------------------        |    --------------------       |   ------------------------------      |
| 1   | Add Blog to Follow List                | `http://127.0.0.1:8000/api/v1/blogs/follow/?blog_id=5`   | Blog ID, User ID                           | -                                 |
| 2   | Create Blog                             | `http://127.0.0.1:8000/api/v1/blogs/createblog/`        | Owner ID, Description, Name, Banner, Blog Photo | -                                 |
| 3   | Create Post                             | `http://127.0.0.1:8000/api/v1/posts/create/`            | Title, Photo List (0 or More), Content, Date, Blog ID, Author ID | -                                 |
| 4   | Write Comment                           | `http://127.0.0.1:8000/api/v1/posts/comment/create`     | User ID, Post ID, Content                  | -                                 |
| 5   | Create New User                         | `http://127.0.0.1:8000/api/v1/accounts/register`        | User Name, First Name, Last Name, Profile Photo, Email, Password | -                                 |
| 6   | Add Like                                | `http://127.0.0.1:8000/api/v1/posts/like/?user_id=3&post_id=3` | User ID, Post ID                       | -                                 |
|---- |     UPDATE METHODS                 |   --------------------- |   ---------------- |      -------------------------------------------- |
| 1   | Update Profile                          | `http://127.0.0.1:8000/api/v1/accounts/update`          | User ID, User Name (Optional), First Name (Optional), Last Name (Optional), Profile Photo (Optional), Email (Optional), Password (Optional) | -                                 |
| 2   | Update Comment                          | `http://127.0.0.1:8000/api/v1/posts/comments/update/4/` | Comment ID, Content                        | -                                 |
| 3   | Update Post                             | `http://127.0.0.1:8000/api/v1/posts/update/?post_id=2`  | Post ID, Content                           | -                                 |
| 4   | Update Blog                             | `http://127.0.0.1:8000/api/v1/blogs/update/?blog_id=1`  | Blog ID, Banner, Blog Photo, Description  | -                                 |
|-----|      DELETE METHODS             |    ----------------------------------------- |     -----------------------------   | --------------------     |
| 1   | Delete Blog from Follow List           | `http://127.0.0.1:8000/api/v1/blogs/unfollow/[blog_id]/` | Blog ID, User ID                           | -                                 |
| 2   | Delete Blog                             | `http://127.0.0.1:8000/api/v1/blogs/delete/6`           | Blog ID                                   | -                                 |
| 3   | Delete Post                             | `http://127.0.0.1:8000/api/v1/posts/delete/9/`         | Post ID                                   | -                                 |
| 4   | Delete User                             | `http://127.0.0.1:8000/api/v1/accounts/update`          | User ID                                   | -                                 |
| 5   | Delete Comment                          | `http://127.0.0.1:8000/api/v1/posts/comments/update/6/` | Comment ID                               | -                                 |
| 6   | Delete Like                             | `http://127.0.0.1:8000/api/v1/posts/like/delete/3`      | -                                         | -                                 |


## User Stories

### User Story 1: Account Creation

As a user, I want to create a new account using my email and password so that I can start using the social media platform.

**Feature Tasks:**

- Design and implement a registration form
- Set up email verification process
- Create a secure password storage mechanism
- Develop error handling for invalid inputs
- Store user account information in the database

**Acceptance Tests:**

- Verify that users receive a verification email upon registration
- Test account creation with valid and invalid inputs
- Ensure passwords are securely stored and hashed
- Check that user account details are correctly stored in the database

**Estimated Size: Small**

### User Story 2: Posting Text Updates

As a user, I want to post text updates on my profile so that I can share my thoughts and activities with my friends.

**Feature Tasks:**

- Design a post composition interface
- Implement text input and formatting options
- Enable posting to the user's profile
- Add real-time updating of the user's feed
- Implement privacy settings for posts

**Acceptance Tests:**

- Test posting with various text lengths and formats
- Verify that posts appear on the user's profile and followers' feeds
- Check that privacy settings restrict post visibility as intended

**Estimated Size: Small**

### User Story 3: Following Other Users

As a user, I want to follow other users' profiles so that I can stay updated on their posts and activities.

**Feature Tasks:**

- Design a user profile interface
- Implement a "Follow" button on user profiles
- Develop a system for tracking followers and following
- Add a feed displaying posts from followed users

**Acceptance Tests:**

- Test following and unfollowing different profiles
- Verify that the follower/following counts update correctly
- Check that the user's feed displays posts from followed users

**Estimated Size: Small**

### User Story 4: Uploading Images

As a user, I want to upload images to my posts so that I can share visual content with my friends.

**Feature Tasks:**

- Enhance the post composition interface to support image uploads
- Implement image upload and storage mechanisms
- Ensure images are properly compressed and optimized
- Display uploaded images within posts and on user profiles

**Acceptance Tests:**

- Test image upload with various image formats and sizes
- Verify that uploaded images are displayed correctly in posts
- Check that images do not affect the platform's performance negatively

**Estimated Size: Medium**

### User Story 5: Liking and Commenting

As a user, I want to like and comment on posts made by other users so that I can engage with their content.

**Feature Tasks:**

- Add "Like" and "Comment" buttons to posts
- Implement the ability to like and unlike posts
- Enable users to write and post comments on others' posts
- Display likes and comments counts on posts

**Acceptance Tests:**

- Test liking and unliking posts
- Verify that comments can be added, edited, and deleted
- Check that likes and comments counts accurately reflect user interactions

**Estimated Size: Small**

Remember, these user stories are just a starting point. As your project progresses, you may need to refine, expand, or reprioritize them based on feedback and changing requirements. Each user story should represent a discrete piece of functionality that can be developed, tested, and deployed independently.

## Software Requirements

### Vision

The vision of our social media platform is to provide users with a dynamic and engaging online space where they can connect, share their thoughts and experiences, and create meaningful relationships with their friends and followers. This project aims to address the need for a platform that fosters genuine interactions, facilitates content sharing, and promotes positive engagement among users.

### Pain Point

Our project solves the pain point of users feeling disconnected and overwhelmed on existing social media platforms. Many users find it challenging to filter through irrelevant content and maintain authentic connections. Our platform strives to create a more personal and focused social experience, where users can engage with content that matters to them and build meaningful relationships.

### Why Care

In today's digital age, social media has become a central part of our lives. However, current platforms often prioritize quantity over quality of interactions. Our product offers a fresh perspective by prioritizing meaningful connections, relevant content, and a user-friendly experience. By addressing the drawbacks of existing platforms, we aim to provide users with a space where they can truly connect and engage.

### Scope (In/Out)

**IN - What Our Product Will Do**

- User Profiles: Users can create profiles, including profile pictures and personal information.
- Content Sharing: Users can create and post text, images, and videos to share with their followers.
- Interactions: Users can like, comment, and share posts created by others.
- Friend/Follow System: Users can follow and befriend other users to see their posts in their feed.

**OUT - What Our Product Will Not Do**

- Messaging Platform: Our product will not have a dedicated messaging feature for private conversations.
- E-commerce Integration: Our product will not facilitate direct sales of products within the platform.

**Minimum Viable Product (MVP) vs. Stretch Goals**

**MVP Functionality:**

- User Profiles and Authentication
- Content Sharing (Text and Images)
- Interactions (Likes and Comments)
- Friend/Follow System

**Stretch Goals:**

- Video Content Sharing
- Advanced Privacy Settings
- Analytics Dashboard for Users

### Functional Requirements

**User Account Management:**

- An admin can create and delete user accounts.
- Users can update their profile information.

**Content Creation and Interaction:**

- Users can create and post text updates with optional images.
- Users can like and comment on posts created by other users.
- Users can follow other users to see their posts in their feed.

### Data Flow

1. User logs in or signs up.
2. User creates a post (text with optional image).
3. User's post is displayed in their profile and followers' feeds.
4. Other users can like and comment on the post.

### Non-Functional Requirements

- **Security:** Our platform will implement industry-standard encryption protocols for data transmission and storage to ensure the privacy and security of user information and interactions. User passwords will be securely hashed and salted before storage.

- **Usability:** Our platform will prioritize user-friendly design, intuitive navigation, and responsive layout to ensure a seamless and enjoyable user experience. User feedback and usability testing will be conducted to continuously improve the platform's usability.

## Setup

Before you begin, ensure that Python 3.10 is installed on your system and that you are on the latest branch version which currently is: ```v2``` .

 Follow these steps to set up and run the API:

1. **Install Dependencies**: Open your terminal and run the following command to install all project dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Apply model changes to database schema**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Start the API**: To start the API, use the following command:

    ```bash
    python manage.py runserver
    ```

    This will launch the API, and you can access it at the provided URL.


## Contributors

- [Ibraheem Areeda](https://github.com/ibraheem-areeda)
- [EmanObeidat](https://github.com/EmanObeidat)
- [swmones](https://github.com/11mones)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Special thanks to [Django rest framework](https://www.django-rest-framework.org/).
- Hat tip to anyone whose code was used.
- Inspiration.
- etc.
