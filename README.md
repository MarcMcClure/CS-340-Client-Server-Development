# CS-340-Client-Server-Development

### About the Project ###
This project provides an interface to search for candidate search-and-rescue dogs in the Austin, Texas area by pulling from a local version of the Austin Animal Center database. With minor modifications AAC_CRUD.py could be used as a generalized CRUD module but it is currently set up to interface with this databse and this databse only.

### Motivation ###
This is a Global Rain project commissioned by Grazioso Salvare international rescue-animal training company.

### Getting Started ###
These instructions will be for getting this project to run on Linux. To get this project working you will need the MongoDB, Python, The pymongo library, Jupyter Notebook, the CRUD module itself AAC_CRUD.py, the Jupyter Notebook project for testing the CRUD module AAC_CRUD_Tester.ipynb, and the Jupyter Notebook project containing the interface AAC_Database_Interface. First install MongoDB and Jupyter Notebook via Anaconda with the included python distribution from the websites listed below. Next install pymongo running the command “pip install pymongo” in the shell. Import the dataset with mongoimport and set up user and admin accounts in MongoDB from the shell. Screenshots for these three actions are included below. To test the module, then open the Jupyter Notebook project AAC_CRUD_Tester.ipynb in Jupyter Notebook and run the testing cells. Screen shots of the tests being passed is also included below. To run the database interface open the Jupyter Notebook project AAC_Database_Interface. Ipynb in Jupyter Notebook and run the cell.

### Installation ###
  *	MongoDB
    *	https://www.mongodb.com/try/download/community
  *	Anaconda, this includes python and Jupyter Notebook, but you can also install Jupyter Notebook in most python IDS’s using pip
    *	https://www.anaconda.com/products/distribution
  *	AAC dataset
    *	Austin Animal Center. (2020). Austin Animal Center Outcomes [Data set]. City of Austin, Texas Open Data Portal. https://doi.org/10.26000/025.000001

### Usage ###
The videos in this repository demonstrate the capabilities of the Database interface. For instructions on using the CRUD module directly see the Code Example section of this document.

  *	Usage Video 1
    *	Starting the interface and opening it in a separate window. 
    *	Scrolling through the interface to show the initial layout.
    *	Click the embedded logo to go to an external website per the client instructions
    *	Showing the filtering option for Water Rescue, Mountain or Wilderness Rescue, Disaster or Individual Tracking, and resetting to show all animals in the database. A drop-down list was used for convenience and clarity. The specifications for each category are as follows.
	
      Rescue Type 	          |Preferred Breeds 	                                                                      |Preferred Sex  |Training Age
      ------------------------|-----------------------------------------------------------------------------------------|---------------|----------------------
      Water	                  |Labrador Retriever Mix, Chesapeake Bay Retriever, Newfoundland	                          |Intact Female	|26 weeks to 156 weeks
      Mountain or Wilderness	|German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, Rottweiler	    |Intact Male	  |26 weeks to 156 weeks
      Disaster or Individual  |Tracking	Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, Rottweiler	  |Intact Male	  |20 weeks to 300 weeks
  *	Usage Video 2
    *	Sorting results by category including multi category sorting.
    *	Filtering animals by keyword search.
    *	Changing how many results are shown per page with a slider.
  *	Usage Video 3
    *	Selecting animals so that their locations show up on the map widget. This widget was used for this functionality because it was specifically asked for by the customer.
    *	Selecting columns to show on the pie chart including multi column selection. A pie Chart was used here to give a general sense of the demographic information of animals across categories. This works best for categories where there is often repeated information like Animal Type, Outcome Type, Breed, Color, Age Upon Outcome, etc. This chart works less well for categories where there is seldom repeated information like Date of Birth. 

### Code Example ###
This section discuses the usage of the AAC CRUD module
This library runs the animal shelter database. First the database must be initialized like this.
		
    animalShelter = AnimalShelter(username, password)	

Entries can be created by using a list of dictionaries or a dictionary like this.
		
    animalShelter.create({"name": "Moe", "age": 8})

or

    animalShelter.create([{"name": "Curly", "age": 6}, {"name": "Larry", "age": 7}])

Entries can be read by using queries formatted in the same way as the find function in MongoDB as documented here. The read function will return a cursor pointing to the first entry in the list. A simple example of this would be this.
		
    animalShelter.read({"name": "Moe"})

this would return a curser that was pointing to the first element in a list of all the entries with the value “Moe” in the key “name”
		
Entries can be Deleted using the same query formatting as the read function. A simple example of this would be this.
		
    animalShelter.delete({"name": "Moe"})

This would delete all entries with the value “Moe” in the key “name”.

### Tests ###
There are 3 blocks of code for testing the python module. They can be run by clicking on each block and pressing the run button or pressing SHIFT + ENTER. Screenshots of these tests being passed are included below.

### Screenshots ###
Importing the dataset into MongoDB.
![image](https://user-images.githubusercontent.com/76132117/235260574-43e1092f-b020-4496-8810-4073ade5adcc.png)

Creating admin and user accounts.
![image](https://user-images.githubusercontent.com/76132117/235260644-b1a5e988-83f8-4a90-bf4a-9732178a6aff.png)
![image](https://user-images.githubusercontent.com/76132117/235260661-282bc325-07bf-4fd7-ae62-b9adbc75a4c7.png)

Jupyter Notebook tests being passed.   
![image](https://user-images.githubusercontent.com/76132117/235260676-b199fd06-7aee-45af-a471-7df55847cf64.png)
![image](https://user-images.githubusercontent.com/76132117/235260683-a7844ae8-026d-44e8-b1fc-31b09d786f12.png)
![image](https://user-images.githubusercontent.com/76132117/235260698-5d582c7b-acb4-4bd8-a1f5-b4095b8941f9.png)

Contact
Marc McClure: mmxman123@gmail.com
