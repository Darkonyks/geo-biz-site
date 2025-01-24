<?php
// Enable error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Log errors to Apache's error log
error_log("Contact form processing started");

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require '../vendor/autoload.php';

// Email configuration
$receiving_email_address = 'office@geo-biz.com';
$smtp_host = 'host107.dwhost.net'; // ili vaš SMTP server
$smtp_username = 'office@geo-biz.com'; // zamenite sa vašim emailom
$smtp_password = 'Remorker1!Geobiz'; // zamenite sa vašom app lozinkom
$smtp_port = 587;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $subject = $_POST['subject'] ?? '';
    $message = $_POST['message'] ?? '';

    // Validate inputs
    $errors = [];
    if (empty($name)) $errors[] = "Name is required";
    if (empty($email)) $errors[] = "Email is required";
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = "Invalid email format";
    if (empty($message)) $errors[] = "Message is required";

    if (empty($errors)) {
        $mail = new PHPMailer(true);

        try {
            // Server settings
            $mail->isSMTP();
            $mail->Host = $smtp_host;
            $mail->SMTPAuth = true;
            $mail->Username = $smtp_username;
            $mail->Password = $smtp_password;
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Port = $smtp_port;

            // Recipients
            $mail->setFrom($smtp_username, 'Contact Form');
            $mail->addAddress($receiving_email_address);
            $mail->addReplyTo($email, $name);

            // Content
            $mail->isHTML(true);
            $mail->Subject = "New Contact Form Message: " . $subject;
            $mail->Body = "
                <h3>You have received a new message:</h3>
                <p><strong>Name:</strong> {$name}</p>
                <p><strong>Email:</strong> {$email}</p>
                <p><strong>Subject:</strong> {$subject}</p>
                <p><strong>Message:</strong><br>{$message}</p>
            ";
            $mail->AltBody = "
                You have received a new message:
                Name: {$name}
                Email: {$email}
                Subject: {$subject}
                Message: {$message}
            ";

            $mail->send();
            error_log("Email sent successfully to " . $receiving_email_address);
            echo json_encode(["success" => true, "message" => "Message sent successfully!"]);
        } catch (Exception $e) {
            error_log("Failed to send email. Error: " . $mail->ErrorInfo);
            echo json_encode(["success" => false, "message" => "Failed to send message. Error: " . $mail->ErrorInfo]);
        }
    } else {
        error_log("Form validation errors: " . implode(", ", $errors));
        echo json_encode(["success" => false, "message" => "Validation errors: " . implode(", ", $errors)]);
    }
    exit;
}
?>
