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
* Reviews section where customers can leave reviews on the products. 
* About section on the landing page

## Technologies Used
### Languages 
* [HTML](https://en.wikipedia.org/wiki/HTML5) 
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 
* [JavaScript](https://www.javascript.com/) 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 

### Frameworks
* [jQuery:](https://jquery.com/): Used for different style effects and functionality throughout the site.
* [Bootstrap 5.01:](https://getbootstrap.com/) Used to style the website and help with the website’s responsiveness. 
* [Google Developer Tools:](https://developer.chrome.com/docs/devtools/) Used to test responsive elements of page and to fix bugs.
* [Git:](https://git-scm.com/)Useful to control and document page versions through git commits and git pushes.
* [Github:](https://github.com/) Used to store project code and to deploy the website.
* [AWS S3:]( https://aws.amazon.com/s3/) Used to store the static data for the live website. These include product images, blog images and js and css files
* [Django:]( https://www.djangoproject.com/) Used in site development to handle user data and python queries to database. 
* [Heroku:]( https://www.heroku.com/) Used to deploy the live version of the site.
* [Balsamiq:](https://balsamiq.com/) Used to draw up wireframes so I could visualise the design of the website.
* [Windows Paint 3D:]( https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab) Used to create a transparent PNGs of the Product images and MMA Cork logo.
* [Color Hunt:]( https://colorhunt.co/) Used to find suitable background colours for styling.   
* [Online-Convert.com:]( https://www.online-convert.com/) Used to convert MMA Cork logo to favicon format.

### Libraries
* [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/installation.html) Used to set up user authentication on the site.
* [Google fonts:](https://fonts.google.com/) Used to find appropriate fonts for the website
* [Font Awesome:](https://fontawesome.com/icons?d=gallery&p=2) Provided the icons for the website buttons and the social media links in the footer. 
*  [Flaticon](https://www.flaticon.com/):  Provided me with a images to display when there was no images on the product card, or when there was no items in the user’s shopping bag. [View here.] 


## Manual Testing
<details>
<summary><b>Site Features</b> - (click to expand)</summary>

### Navbar
- Navbar links working from each page. - PASS
- The main logo takes the user to the welcome page. - PASS
- All navbar links and search icon functioning on off canvas navbar for smaller screens – PASS
- Shopping bag icon displays correct bag total - PASS 

### Footer 
- Links working from each page. - PASS
- Newsletter sends email to user email if inputted – PASS
- Newsletter doesn’t accept sane email twice – PASS

### Landing Page
* Visit store link working on all screen sizes – PASS
* Hero image displaying neatly on all screen sizes – PASS

### Products Page
* Correct product count on page – PASS
* Sort filters working – PASS
* Product cards displaying neatly on all screen sizes
* Category links on cards working – PASS
* Clicking on card image brings you to product details page – PASS
* Edit/Delete links on product cards working for admin user – PASS

### Product Details
* Carousel displaying front and back images functioning correctly - PASS
* Product info displaying correctly – PASS
* Quantity input bar does not go below 1 or above 99 – FAIL
* Size dropdown functioning correctly – PASS
* Edit/Delete links working for admin users
* Edit/Delete links not visible to regular users
* Edit/Delete functionality unavailable to user if correct URL inputted – PASS
* Add to Bag and Keep Shopping button links functioning - PASS

### Allauth
* Email confirmation required when signing up - PASS
* User cannot log in if no account created - PASS
* User cannot login with incorrect username/email/password - PASS
* User cannot create account with email/username that’s already in use – PASS

### Shopping Bag
* Shopping bag displays correct product info (image, title, size, quantity) – PASS
* Update quantity input working on mobile and larger screens – PASS
* User cannot input number under 1 or over 99 in quantity input – FAIL
* Subtotal on larger screen calculates correct price when quantity input updated – PASS
* Remove item button working on small and large screens – PASS
* Bag total calculates correct total for large and small screens - PASS
* Empty shopping bag html displays when no items in bag – PASS
* Secure checkout and Keep shopping buttons linking to correct pages – PASS

### Blog
* Blog info (image, title, update info) displaying correctly – PASS
* Comments displaying under Blog post
* Comments display username, date/time the comment was uploaded – PASS
* User can upload comment using form below comment field – PASS
* Admin able to add blog post from site - PASS
* Admin able to edit existing blog posts - PASS
* Admin able to delete existing blog posts - PASS
* Regular user unable to create blog post - PASS
* Regular user unable to edit blog post – PASS
* Regular user unable to delete blog post – PASS

### Checkout
* Checkout form rendering correctly on large and small screens - PASS
* Cannot complete order without inserting Full Name, Phone Number, Street Address 1, Town, Country, Card Number, Card Expiration Date, Card Postal Code - PASS
* Required order fields do not accept white space – PASS
* User’s previously saved info in profile already inputted into fields – PASS
* Order Summary displaying correct info and correct total – PASS
* Stripe receiving payment webhooks – PASS
* Payment Success/Error messages displaying correctly – PASS
* User directed to order summary - PASS  


### Profile
* Profile displaying Delivery info form – PASS
* Profile does not display order history table if there is no order history – PASS
* Profile saves delivery info for use in checkout page – PASS
* User can view previous order history in order history section – PASS
* Order number link brings user to page with order details – PASS

</details>

<details>
<summary><b>User Stories</b> - (click to expand)</summary>
#### Regular User

As a regular user, I want: 
1. A visually appealing site no matter what device I use.
* Bootstrap styling makes the site responsive and appealing at all screen sizes. 
2. To be able to intuitively navigate through the site the first time I visit.
* Conventional structure of the site ensures that the user will intuitively know how to navigate through the page.
3. The site’s purpose to be clear on the landing page
* General sense of what the website is about. However, it does need an about section that explains the site’s purpose in more detail.
4. The ability to log in and out of the site once I am registered to make future purchases easier.
* Users can log in/out with ease and they can save their delivery information to their profile once registered. This will then be seen on the checkout page
5. Access to my order history in my profile and delivery information.
* Order history will display under the user’s delivery information on their profile.
6. The ability to search for products on the site using keywords.
* Search bar at the top of page will return results found in the product’s title, category, or description.
7. To sort all available products based on price/name/category.
* User can select the input on the products page which can sort the product by their name, rating, and price. The Product dropdown in the navbar sorts the products by their category.
8. The ability to view more information on a certain product if I am interested in it.
* User can click on the product image to take them to the product details page. From here the user can see the description of the product and add it to their bag.
9. To view/leave reviews on a product.
* This feature has not been implemented.
10. To add items to a basket if I want to buy more than one product.
* Add to basket option in product details page. From here the user can continue shopping and can select the link in the navbar to go to their basket when they are finished browsing.
11. The ability to update items when they are in my basket.
* User can update the product quantity or remove the item from their basket on the basket page.
12. The ability to contact the gym if I need more information on products. 
* Gym contact info in page footer 
13. Receive confirmation that my purchase was successful upon checking out. 
* User will see a notification pop up informing them of a successful/unsuccessful order. The user will then be directed to a page with their order details. They can also view these details in the order history section of their profile.

#### Store Owner
As a store owner, I want:
1. To be able to easily add products to the store.
* Product management section in account dropdown where admin can add products from live site.
2. The ability to edit a product’s details e.g price/image etc.
* Edit link in product/product details page that directs them to a form where the admin can edit the product details.
3. To be able to delete products from my store that are no longer available/popular.
* Delete link in products/product details page.
4. The ability to add/edit blog posts, so that users know the story behind the gym and clothing.
* Add Post button just under heading on blog page that directs admin to form to enter blog details.
* Edit Post link under blog image on blog and post page. 
5. The ability to delete blog posts.
* Delete Post link under blog image on blog and post page
6. The ability to delete product reviews if unsuitable.
* Product reviews functionality not implemented.

#### Software Developer/Recruiter
As a software developer/recruiter, I want: 
1. To view the developer’s Linked In profile
* Link to my LinkedIn profile in the website footer
2. To view the developer’s GitHub repository for the project so I can look at their code.
* Link to the project’s GitHub repository in the footer of the website 
3. The ability to examine the creator’s ReadMe for more details on how the project was created.
4. View the site and play around with its features e.g fake purchases
* Live site deployed to Heroku and sample card provided to users in at the top of the project ReadMe. This will allow users to view the site, comment on blog posts and make fake purchases.

</details>

<details>
<summary><b>Responsive Design</b> - (click to expand)</summary>

The website layout was tested on the following physical devices: 
* Huawei P20 Lite (Google Chrome)
* iPad (Safari)
* Fujitsu Lifebook A512 (Google Chrome)
* Hp L1906 (Google Chrome)

Google Chrome Developer Tools was also used to test the responsiveness of the site using the following devices. 
* Moto G4 
* Galaxy S5
* Pixel 2 
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold
* Nest Hub
* Nest Hub Max

### Browser Compatibility
Browser compatibility was physically tested across the different browsers listed below: 
* Google Chrome Version 89.0.43389.114
* Microsoft Edge Version 89.0.774.68
* Mozilla Firefox Version 87.0

No problems were found

</details>



