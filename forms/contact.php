<?php
// Enable error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Log errors to Apache's error log
error_log("Contact form processing started");

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require '../vendor/autoload.php';

// Email configuration — učitava se iz config.php (van Git-a).
// Kopirajte config.example.php u config.php i popunite vrednosti.
$config_file = __DIR__ . '/config.php';
if (!file_exists($config_file)) {
    error_log("Missing config.php in forms/ directory");
    http_response_code(500);
    echo json_encode(["success" => false, "message" => "Server configuration error."]);
    exit;
}
$config = require $config_file;

$receiving_email_address = $config['receiving_email_address'];
$smtp_host     = $config['smtp_host'];
$smtp_username = $config['smtp_username'];
$smtp_password = $config['smtp_password'];
$smtp_port     = $config['smtp_port'];
$smtp_encryption = $config['smtp_encryption'] ?? 'tls';   // 'tls' (587) ili 'ssl' (465)
$smtp_debug      = $config['smtp_debug'] ?? 1;             // 1 = upiši SMTP dijalog u error_log

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
            if ($smtp_debug) {
                $mail->SMTPDebug = 2;            // detaljan SMTP dijalog
                $mail->Debugoutput = 'error_log'; // u log, da ne pokvari JSON odgovor
            }
            $mail->isSMTP();
            $mail->Host = $smtp_host;
            $mail->SMTPAuth = true;
            $mail->Username = $smtp_username;
            $mail->Password = $smtp_password;
            $mail->SMTPSecure = ($smtp_encryption === 'ssl')
                ? PHPMailer::ENCRYPTION_SMTPS      // SSL, obično port 465
                : PHPMailer::ENCRYPTION_STARTTLS;  // TLS, obično port 587
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
