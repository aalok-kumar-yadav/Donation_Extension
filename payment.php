<?php
include("db.php");
?>
<!DOCTYPE html>
 <head>
  <html lang="en">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width", intial-scale=1,shrink-to-fit=no">
    <link href="https://fonts.googleapis.com/css?family=Oleo+Script:400,700" rel="stylesheet">
   	<link href="https://fonts.googleapis.com/css?family=Teko:400,700" rel="stylesheet">
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css">
   <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
<section id="contact">
			<div class="section-content">
				<h1 class="section-header"> <span class="content-header wow fadeIn " data-wow-delay="0.2s" data-wow-duration="2s"> Be The Reason for Someone's Smile </span></h1>
				
			</div>
			    <form  id="form" method="post" action="form_action.php" enctype="multipart/form-data">
					<div class="col-md-6 form">
			  			<div class="form-group">
			  				<label for="exampleInputUsername">Your name</label>
					    	<input type="text" class="form-control" name="name" placeholder=" Enter Name">
				  		</div>
				  		<div class="form-group">
					    	<label for="exampleInputEmail">Email Address</label>
					    	<input type="email" class="form-control" name="email" placeholder=" Enter Email id">
					  	</div>	
					  	<div class="form-group">
					    	<label for="text">State</label>
					    	<input type="text" class="form-control" name="state" placeholder=" Enter your state.">
			  			</div>
			  			<div class="form-group">
					    	<label for="text">Amount</label>
					    	<input type="text" class="form-control" name="amount" placeholder="Enter your amount">
			  			</div>
			  			<div class="form-group">
					    	<label for="text">Transcation Id</label>
					    	<input type="text" class="form-control" name="txnid" value="<?php echo $txnid=rand(1000000000,9999999999)?>">
			  			</div>
			  			
			  		
			  		
			  			<div id="submit_div">
                            <button type="submit" class="btn btn-default submit" name="submit"><i class="fa fa-paper-plane" aria-hidden="true"></i> Submit </button>
			  			</div> 

			  			
				
				</form>
			
		</section>
		
		</body>
		</html>
		
	   
