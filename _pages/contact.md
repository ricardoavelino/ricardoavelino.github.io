---
layout: clean
nav: contact
permalink: /contact/
title: "Contact"
---

<h1 class="page-title">Contact</h1>
<p class="lead">A question, an idea, or a collaboration? Send me a message and it lands in my inbox.</p>

<form class="contact-form reveal" action="https://formsubmit.co/mricardo@ethz.ch" method="POST">
  <!-- FormSubmit settings -->
  <input type="hidden" name="_subject" value="New message from ricardoavelino.github.io">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_next" value="https://ricardoavelino.github.io/contact/?sent=true">
  <input type="text" name="_honey" style="display:none">

  <div class="field"><label for="cf-name">Name</label>
    <input id="cf-name" type="text" name="name" autocomplete="name" required></div>
  <div class="field"><label for="cf-email">Email</label>
    <input id="cf-email" type="email" name="email" autocomplete="email" required></div>
  <div class="field"><label for="cf-title">Title</label>
    <input id="cf-title" type="text" name="title" required></div>
  <div class="field"><label for="cf-msg">Message</label>
    <textarea id="cf-msg" name="message" rows="6" required></textarea></div>

  <button type="submit" class="btn-send">Send</button>
</form>
