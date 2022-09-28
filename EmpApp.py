<!DOCTYPE html>
<html>
<head>
	<title>Add Employee Information</title>
</head>
<style>
	body {
		background-color: white;
	}

	form {
		text-align: center;
	}

	table {
		margin-left: auto;
		margin-right: auto;
	}

	body {
		font-family: 'Montserrat', sans-serif;
		line-height: 1.6;
		margin: 0;
		min-height: 100vh;
		background-color: rgb(222, 190, 148);
	}

	ul {
		margin: 0;
		padding: 0;
		list-style: none;
	}

	.content {
		width: 850px;
		margin: auto;
		margin-bottom: 350px; /* Same height as footer */
		padding: 100px 0;
	}

	.fixed_footer {
		width: 100%;
		height: 200px;
		background: #111;
		position: fixed;
		left: 0;
		bottom: 0;
		z-index: -100;
	}


	.employeeid {
		font-size: 32px;
	}

	.footer_class {
		color: #696969;
		column-count: 2;
		column-gap: 50px;
		font-size: 1em;
		font-weight: 300;
	}

	form {
		text-align: center;
	}

	p {
		text-align: center;
	}

	h2,
	h3,
	a {
		color: #34495e;
	}

	a {
		text-decoration: none;
	}



	.logo {
		margin: 0;
		font-size: 1.45em;
	}

	.main-nav {
		margin-top: 5px;
	}

		.logo a,
		.main-nav a {
			padding: 10px 15px;
			text-transform: uppercase;
			text-align: center;
			display: block;
		}

		.main-nav a {
			color: #34495e;
			font-size: .99em;
		}

			.main-nav a:hover {
				color: #718daa;
			}

	.header {
		padding-top: .5em;
		padding-bottom: .5em;
		border: 1px solid #a2a2a2;
		background-color: #f4f4f4;
		-webkit-box-shadow: 0px 0px 14px 0px rgba(0,0,0,0.75);
		-moz-box-shadow: 0px 0px 14px 0px rgba(0,0,0,0.75);
		box-shadow: 0px 0px 14px 0px rgba(0,0,0,0.75);
		-webkit-border-radius: 5px;
		-moz-border-radius: 5px;
		border-radius: 5px;
	}

	@media (min-width: 769px) {
		.header,
		.main-nav {
			display: flex;
		}

		.header {
			flex-direction: column;
			align-items: center;
			width: 80%;
			margin: 0 auto;
			max-width: 1150px;
		}
	}

	@media (min-width: 1025px) {
		.header {
			flex-direction: row;
			justify-content: space-between;
		}
	}
</style>
<center>
	<font color="black" size="3" style="font-family: avenir">

		<header class="header">
			<ul class="main-nav">
				<li><a href="/gotoaddemp">Add Employee</a></li>
				<li><a href="/getemp">Get Employee</a></li>
				<li><a href="/apply">Apply Leave</a></li>
				<li><a href="/gotoviewallleave">View Leave Status</a></li>
				<li><a href="/gotoapproveleave">Approve Leave</a></li>
				<li><a href="/gotoupdatepayroll">Update Payroll</a></li>
				<li><a href="/gotopayroll">Update Payroll</a></li>
				<li><a href="/gotoattendance">Attendance</a></li>
			</ul>
		</header>

		<h1 style="color: red">Employee Database</h1>

		<body bgcolor="white">

			<form action="/addemp" autocomplete="on" method="POST" enctype="multipart/form-data">

				Employee ID:<br> <input style="height:25px;font-size:14pt; color:grey;border-radius: 30px;" type="number" name="emp_id" autofocus size="40"><br><br>

				First Name:<br> <input style="height:25px;font-size:14pt;color:grey;border-radius: 30px;" type="text" name="first_name"><br><br>

				Last Name:<br> <input style="height:25px;font-size:14pt;color:grey;border-radius: 30px;" type="text" name="last_name"><br><br>

				Primary Skills:<br> <input style="height:25px;font-size:14pt;color:grey;border-radius: 30px;" type="text" name="pri_skill"><br><br>

				Location:<br> <input style="height:25px;font-size:14pt;color:grey;border-radius: 30px;" type="text" name="location"><br><br>

				Job Title:<br> <input style="height:25px;font-size:14pt;color:grey;border-radius: 30px;" type="text" name="job_title"><br><br>

				Gender:<br> <input style="height:25px;font-size:14pt;color:grey;border-radius: 30px;" type="text" name="gender"><br><br>
				
				<label for="dateOfHired">Date of Hired:</label><br>
				<input style="height:25px;font-size:14pt;color:grey;border-radius: 30px;" type="date" id="dateOfHired" name="date_of_hired"><br><br>
				
				Image: <input type=file name="emp_image_file" style="height:25px;font-size:14pt;color:grey;"> <br><br>

				<button type="submit" style="background: orangered; height: 45px; width: 200px; color: white; size: 5; border-radius: 30px;font:oblique;">UPDATE DATABASE</button>

			</form>
		</body>

	</font>
</center>
</html>
