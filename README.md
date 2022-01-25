## Project Description
This website is the final milestone project of the Code Institute Full Stack Web Development Program. The main Technologies used for the site are HTML, CSS, JavaScript, Python and Django.

My final project is an online store that sells training clothing and protein belonging to the MMA Cork gym. The purpose of the site is to allow members to view different products, add these products to their basket and securely purchase their order. 

The user is also able to create an account on the website and view the MMA Cork Blog posts.

It is important to add that this site is not a fully functioning e-commerce store and is solely for educational purchases. You can use the following information below to simulate a card purchase on the store

* Card Number - 4242 4242 4242 4242
* Expiry Date - Any date.
* CVV - Any 3-digit number.

Admin Page Log in Details
* The admin page log in details are as follows. Username: admin. Password: DVDPlayer19

### User Stories 

#### Regular User
As a regular user, I want: 
1. A visually appealing site no matter what device I use.
2. To be able to intuitively navigate through the site the first time I visit.
3. The site’s purpose to be clear on the landing page
4. The ability to log in and out of the site once I am registered to make future purchases easier.
5. Access to my order history in my profile and delivery information.
6. The ability to search for products on the site using keywords.
7. To sort all available products based on price/name/category.
8. The ability to view more information on a certain product if I am interested in it. 
9. To view/leave reviews on a product.
10. To add items to a basket if I want to buy more than one product.
11. The ability to update items when they are in my basket. 
12. The ability to contact the gym if I need more information on products. 
13. To receive confirmation that my purchase was successful upon checking out. 

#### Store Owner
As a store owner, I want:
1. To be able to easily add products to the store.
2. The ability to edit a product’s details e.g price/image etc.
3. To be able to delete products from my store that are no longer available/popular.
4. The ability to add/edit blog posts, so that users know the story behind the gym and clothing.
5. The ability to delete blog posts.
6. The ability to delete product reviews if unsuitable.

#### Software Developer/Recruiter
As a software developer/recruiter, I want: 
1. To view the developer’s Linked In profile
2. To view the developer’s GitHub repository for the project so I can look at their code.
3. The ability to examine the creator’s ReadMe for more details on how the project was created.
4. View the site and play around with its features e.g fake purchases


#### Developer Goals 
My personal goals for this project are as follows: 

As a developer, I want to: 
1. Develop a deeper understanding of JavaScript, Python, and the Django framework by creating an original project.
2. Create a professional looking project that I will be proud to put in my portfolio.

### Wireframes 
I used Balsamiq wireframes create a basic visual of how the main pages of the site would look on desktop  and mobile devices.

You can view the wireframes below.

* [Landing Page](media/landing-page.png)
* [Products Page](media/products-page.png)
* [Product Details](media/product-details.png)
* [Shopping Bag](media/bag.png)
* [Secure Checkout](media/secure-checkout.png)
* [Blog](media/blog.png)
* [Blog Details](media/blog-details.png)

It is important to note that I did not do a wireframe for certain pages as a result of the deadline date for this project. 


## Features 
### Colour Palette
The four main colours I chose for the website are displayed in hex format below. They were chosen after using the gym’s logo as a reference point for the site colours.

* White #F5F5F5: Used for the navbar and the footer background colour
* White #FCFCFC: Used for the body background colour
* Red #F05454: Used for the website buttons and links, and the buttons on the website 
* Black ##121212: Used for the majority of the font colours on the site. 

### Fonts
I used two different fonts for this website
* ['Oxygen', sans-serif:]( https://fonts.google.com/specimen/Oxygen) Used for the website headings
* ['Noto Serif', serif:]( https://fonts.google.com/?query=work+sans) Used for all other font elements of the website. 

### Base Template Features
* Links for dependencies: All relevant CSS, bootstrap, font awesome, JavaScript/jQuery links are coded in the base template. This means that I did not need to input these dependencies into each html page. 
* Navbar: The navbar displays the website logo and all the navbar links. The user can only see certain navbar links depending on if they are logged in/out, or if they are admin/regular user. This was done through the use of Django conditional statements. 
* Footer: The footer features all relevant social links. It also features a newsletter input where the user can input their email to subscribe. The email will then be saved to the admin site under subscribers and an automatic email will be sent to the user thanking them for their subscription.
* Toast Functionality: The toasts container is loaded on the base template which allows the notifications to display on all pages. 
 	

### Home Page Features
* Hero Image: The landing page has a hero image with a short heading within. This image covers the whole width of the page and has custom CSS styling to darken it. This allows the heading to the side of the image to stand out more. 
* View Store: There is a visit store button on the left-hand side of the screen within the hero image that allows users to visit the store. This will bring users to the products page.

### Log In/Register Features
* The [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
plug in was used to handle authentication, registration and general account management on the site.
* Registration: The user must input their email and password twice to register. The user must also enter a username.
* Log In: User must input the correct email and password that they used to register. The validation is then run through allauth validation
* These forms were then styled using [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)


### Profile Features
* A user’s profile displays the user’s default delivery info. If the user has made an order, a table with their order history will also show up under their delivery info. The user can look at the order info from the table.


### Products Page Features
* Bootstrap cards display the product images and details.
* Product details include name, price, category, and rating.
* When the user hovers over the image with their mouse, they will see the product description.
* If there is no image for the product, a default image will be displayed.
* Product count will be displayed on the left of the screen just under the header
* An input which allows you to sort the products by name, price and rating is on the right side of the screen just under the heading 
* Users will be directed to the product details page when they click on the product image
* Admin users can edit and delete these products using the Edit and Delete options in the bootstrap cards. These are not visible to normal users.

### Product Details Features
* Features a carousel that displays images of the product from the front and back. This is on the left side in larger screens and takes up the whole width of the screen on smaller devices.
* The product details are shown on the right side of the screen on large screens and under the carousel on small screens.
* The user can choose the size and quantity of the product from the product details page. These can be selected under the product description.
* The user can add the product to their bag from the button on the bottom of the page or they can go back to the products page by selecting the ‘Keep Shopping’ button
* Admin users can edit/delete the product from this page also by using the links beside the product rating.
 

### Shopping Bag Features
* This page displays the products the user has added to their bag. These will be displayed in table format on large screens and as full width divs on small screens.
* The table displays the product info, gives the user the price of the product and calculates the subtotal of that line. The subtotal increases if you get two of the same products at the same size.
* The user can update the quantity of the product in the shopping bag. They can also remove the product if they want to.
* The bag total can be seen at the bottom of the screen and is calculated by adding up the subtotal columns.
* From here the user can go to the checkout page and input their delivery and card info.


### Secure Checkout Features
* There is a section where the user has to input their delivery info. They can also check the input box at the end of the screen to save this info to their profile. 
* The user must then input their card details. The handling of these details is dealt with by the [Stripe API]( https://stripe.com/docs/payments/payment-methods)
* There is also an order summary section on the checkout page that displays the order details, including the product image, title, size, quantity, and the order total.

### Blog
* The blog page features different blog posts created by the site admin. The posts are displayed in card format similar to the products.
* The blog cards contain an image and the blog details. The user can then click on the blog image or the button at the end of the card to see the blog post.
* Admin users are able to edit and delete these blog posts by clicking the links under the blog image.
* There is also an option just under the page header that allows admin users to add a new blog post.

### Blog Post Page Features
* This page displays the blog post title at the top, the post image below and then the blog post text.
* The user can see when the admin created the post just under the image. 
* The user can also see any comments left by other users in the comment section under the blog text
* The user can also leave a comment under the blog by inputting their info into the form at the bottom of the page.

### Admin Extra Features 
* The admin has an extra ‘Product Management’ link that allows them to add a new product to the store. 
* The admin also has the power to delete or edit any product/blog post that is on the site. This is to ensure that all product/blog cards look clean and that there are no inappropriate cards on the site.

### Admin Page Log in Details
* The admin page log in details are as follows. Username: admin. Password: DVDPlayer19

### Future Features
* Discount Feature: A discount feature that targets specific categories of products depending on the season.
* Pagination: Create pagination for the product and blog pages.


