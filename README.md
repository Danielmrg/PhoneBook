# Phone Book

This site is an audience management system. Where some contact details are stored. These specifications include code name and description description.

- Project link in [Github](https://github.com/Danielmrg/PhoneBook)
- Project link in [Online](http://programer24.pythonanywhere.com/)

[[_TOC_]]

## Prototype

![prototype](/uploads/65d154c04533a11ceeb3856dea02970e/4.PNG "prototype")

## About first page (main page)

this here we can see any contact an we can search is this page 

![1](/uploads/fa8c1754ed27fcf4079822c88f87a094/1.PNG "Page Home")

## Create new contact

Here it receives and stores the user details and transfers the user to another page.

![2](/uploads/16ebfabec26d9f02bca75df2a624fa20/2.PNG "create contact")

## Add phone number for contact

In this part you will receive the contact's phone number and then it will take you to the main page.

![3](/uploads/d05fa033cc7d4a837c5fc89b91cbe1c2/3.PNG "Add Phone Number")

## About how its works

Each contact has a first and last name. But it can have one or more phone numbers.

```mermaid
graph TD;
  Contact-->First-Name;
  Contact-->Last-Name;
  Contact-->Description;
```


```mermaid
graph TD;
  Contact-->Phone-Number;
  Contact-->Phone-Number;
  Contact-->Phone-Number;
```
## Equipment was used.

- [x] Equipment was used.
  - [x] Framework Backend: Django
  - [x] Frontend : Html , Css , Js and bootstrap4
  - [x] Host : python anywhere

## Team

 - [x] @DanielMRG 
