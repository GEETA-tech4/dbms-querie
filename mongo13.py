use TECSD; 
db.createCollection("Teachers");
db.createCollection("Students");


db.Teachers.insertMany([
    { "Thame": "Praveen", "dno": 101, "dname": "CSD", "experience": 5, "salary": 8000, "date_of_joining": new Date("2019-01-15") },
    { "Thame": "Rajesh", "dno": 102, "dname": "IT", "experience": 7, "salary": 12000, "date_of_joining": new Date("2018-05-22") },
    { "Thame": "Hitesh", "dno": 103, "dname": "Computer", "experience": 4, "salary": 9000, "date_of_joining": new Date("2020-06-01") },
    { "Thame": "Anjali", "dno": 104, "dname": "CSD", "experience": 3, "salary": 7000, "date_of_joining": new Date("2021-03-10") },
    
]);

// Students Collection Sample Data
db.Students.insertMany([
    { "Sname": "Amit", "roll_no": 1, "class": "10A" },
    { "Sname": "Hitesh", "roll_no": 2, "class": "12B" },
    { "Sname": "Sita", "roll_no": 3, "class": "9C" },
    { "Sname": "Raj", "roll_no": 4, "class": "11D" }
]);

db.Teachers.find().pretty();  // Display all teacher information
db.Teachers.find({ "dname": "CSD" }).pretty();  // Teachers in CSD department
db.Teachers.find({ "dname": { $in: ["Computer", "IT", "CSD"] } }).pretty();  // Teachers in multiple departments
db.Teachers.find({ 
    "dname": { $in: ["Computer", "IT", "CSD"] }, 
    "salary": { $gt: 10000 } 
}).pretty();  // Teachers in Computer, IT, and CSD departments with salary greater than 10000
db.Students.find({ 
    $or: [ { "roll_no": 2 }, { "Sname": "Hitesh" } ] 
}).pretty();  // Students with roll_no = 2 or name "Hitesh"
db.Teachers.updateOne(
    { "Thame": "Praveen" },  // Find Praveen
    { $set: { "experience": 10 } },  // Update experience to 10
    { upsert: true }  // If the teacher doesn't exist, insert as new
);
db.Teachers.updateMany(
    { "dname": "IT" },  // Find all teachers in IT department
    { $set: { "dname": "CSD" } }  // Update their department to CSD
);
db.Teachers.find({}, { "Thame": 1, "experience": 1, "_id": 0 }).pretty();  // Display teacher names and their experience
db.Teachers.deleteMany({ "dname": "IT" });  // Delete all teachers in the IT department
db.Teachers.find().sort({ "Thame": 1 }).limit(3).pretty();  // Sort by name in ascending order and display first 3






