document.addEventListener("DOMContentLoaded", () => {
  // 1. Sticky Navbar Effect
  const navbar = document.getElementById("navbar");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  });

  // 2. Scroll Reveal Animation using Intersection Observer
  const revealElements = document.querySelectorAll(".reveal");

  const revealOptions = {
    threshold: 0.15, // Trigger when 15% of the element is visible
    rootMargin: "0px 0px -50px 0px",
  };

  const revealOnScroll = new IntersectionObserver(function (entries, observer) {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        return;
      }
      entry.target.classList.add("active");
      // Optional: Stop observing once revealed to only animate once
      observer.unobserve(entry.target);
    });
  }, revealOptions);

  revealElements.forEach((el) => {
    revealOnScroll.observe(el);
  });

  // 3. FAQ Accordion Logic
  const faqItems = document.querySelectorAll(".faq-item");

  faqItems.forEach((item) => {
    const question = item.querySelector(".faq-question");

    question.addEventListener("click", () => {
      // Close other open items
      faqItems.forEach((otherItem) => {
        if (otherItem !== item && otherItem.classList.contains("active")) {
          otherItem.classList.remove("active");
        }
      });

      // Toggle current item
      item.classList.toggle("active");
    });
  });

  // 4. Smooth Scrolling for Anchor Links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href");

      // Ignore empty hashes or just '#'
      if (targetId === "#") return;

      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        e.preventDefault();
        // Offset for fixed header
        const headerOffset = 80;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition =
          elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: "smooth",
        });
      }
    });
  });
  // ==========================================
  // 5. AUTH MODAL LOGIC (LOGIN / SIGNUP)
  // ==========================================
  const modal = document.getElementById("auth-modal");
  const loginBtns = document.querySelectorAll(".open-login");
  const signupBtns = document.querySelectorAll(".open-signup");
  const closeBtn = document.querySelector(".close-btn");
  const tabBtns = document.querySelectorAll(".tab-btn");
  const modalTitle = document.getElementById("modal-title");
  const submitBtn = document.getElementById("auth-submit-btn");
  const signupOnlyFields = document.querySelectorAll(".signup-only");

  function openModal(tab) {
    modal.classList.add("active");
    switchTab(tab);
  }

  function closeModal() {
    modal.classList.remove("active");
  }

  function switchTab(tab) {
    tabBtns.forEach((btn) => {
      if (btn.dataset.tab === tab) {
        btn.classList.add("active");
      } else {
        btn.classList.remove("active");
      }
    });

    if (tab === "login") {
      modalTitle.textContent = "Welcome Back";
      submitBtn.textContent = "Login";
      signupOnlyFields.forEach((field) => (field.style.display = "none"));
    } else if (tab === "signup") {
      modalTitle.textContent = "Create an Account";
      submitBtn.textContent = "Sign Up";
      signupOnlyFields.forEach((field) => (field.style.display = "block"));
    }
  }

  loginBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      openModal("login");
    });
  });

  signupBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      openModal("signup");
    });
  });

  tabBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      switchTab(e.target.dataset.tab);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener("click", closeModal);
  }

  window.addEventListener("click", (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  // ==========================================
  // 6. TÍCH HỢP FETCH API CHO LOGIN / SIGNUP
  // ==========================================
  const authForm = document.getElementById("auth-form");
  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");

  // URL
  const BASE_URL = "http://127.0.0.1:8000";

  authForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const isLogin = document
      .querySelector('.tab-btn[data-tab="login"]')
      .classList.contains("active");

    const payload = {
      email: emailInput.value,
      password: passwordInput.value,
    };

    if (!isLogin && nameInput.value) {
      payload.name = nameInput.value;
    }

    const endpoint = isLogin ? "/login" : "/register";

    try {
      submitBtn.textContent = "Handling...";
      submitBtn.disabled = true;

      const response = await fetch(`${BASE_URL}${endpoint}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (response.ok) {
        if (data.user_id) {
          localStorage.setItem("user_id", data.user_id);
        }
        window.location.href = "index.html";
      } else {
        alert(`Lỗi: ${data.detail || "ERROR, Try again!"}`);
      }
    } catch (error) {
      console.error("Error connecting to server:", error);
      alert("Can not connect to server. Please try again later.");
    } finally {
      submitBtn.textContent = isLogin ? "Login" : "Sign Up";
      submitBtn.disabled = false;
    }
  });
});
