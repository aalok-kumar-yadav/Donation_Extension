<?php
 include('db.php');
			if (isset($_POST['submit']))
			 {
				echo $name=$_POST['name'];
				echo $email=$_POST['email'];	
			    echo $state=$_POST['state'];	
				echo $amount=$_POST['amount'];
				echo $txnid=$_POST['txnid'];

             $sql=mysql_query("insert into payment( name,email,state,amount,txnid)
			    value('$name','$email','$state','$amount','txnid')");
                $MARCHENT_KEY="yTJh00";
				$SALT= "XbY4E4wP";
			$hashseq= $MARCHENT_KEY.'|'.$txnid.'|'$amount.'|'.$name.'|'.$email.'|||||||||||'.$SALT;
			$hash="strlower(hash("sha512",$hashseq));
			 
	}
}
?>
<!DOCTYPE html>
<html>
<script>
   function submitForm()
   {
      var postFrom=document.forms.postForm;
	  postForm.submit();
   }
   </head>
   <body>
   </body>
   </html>
</script>