// Custom cursor animation
document.addEventListener('DOMContentLoaded', function() {
  const cursor = document.querySelector('.cursor');
  const cursorFollower = document.querySelector('.cursor-follower');
  
  // Move cursor
  document.addEventListener('mousemove', function(e) {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
    
    // Delay the follower for a trailing effect
    setTimeout(function() {
      cursorFollower.style.left = e.clientX + 'px';
      cursorFollower.style.top = e.clientY + 'px';
    }, 100);
  });
  
  // Cursor hover effects
  const hoverElements = document.querySelectorAll('a, button, .select2-selection, .weight-bar-container');
  
  hoverElements.forEach(el => {
    el.addEventListener('mouseenter', function() {
      cursor.style.transform = 'translate(-50%, -50%) scale(1.5)';
      cursor.style.backgroundColor = 'var(--primary)';
      cursorFollower.style.transform = 'translate(-50%, -50%) scale(0.5)';
    });
    
    el.addEventListener('mouseleave', function() {
      cursor.style.transform = 'translate(-50%, -50%) scale(1)';
      cursor.style.backgroundColor = 'var(--secondary)';
      cursorFollower.style.transform = 'translate(-50%, -50%) scale(1)';
    });
  });
  
  // Initialize particles.js
  if (document.getElementById('particles-js')) {
    particlesJS('particles-js', {
      particles: {
        number: {
          value: 80,
          density: {
            enable: true,
            value_area: 800
          }
        },
        color: {
          value: "#6c5ce7"
        },
        shape: {
          type: "circle",
          stroke: {
            width: 0,
            color: "#000000"
          },
          polygon: {
            nb_sides: 5
          }
        },
        opacity: {
          value: 0.5,
          random: false,
          anim: {
            enable: false,
            speed: 1,
            opacity_min: 0.1,
            sync: false
          }
        },
        size: {
          value: 3,
          random: true,
          anim: {
            enable: false,
            speed: 40,
            size_min: 0.1,
            sync: false
          }
        },
        line_linked: {
          enable: true,
          distance: 150,
          color: "#6c5ce7",
          opacity: 0.4,
          width: 1
        },
        move: {
          enable: true,
          speed: 2,
          direction: "none",
          random: false,
          straight: false,
          out_mode: "out",
          bounce: false,
          attract: {
            enable: false,
            rotateX: 600,
            rotateY: 1200
          }
        }
      },
      interactivity: {
        detect_on: "canvas",
        events: {
          onhover: {
            enable: true,
            mode: "grab"
          },
          onclick: {
            enable: true,
            mode: "push"
          },
          resize: true
        },
        modes: {
          grab: {
            distance: 140,
            line_linked: {
              opacity: 1
            }
          },
          bubble: {
            distance: 400,
            size: 40,
            duration: 2,
            opacity: 8,
            speed: 3
          },
          repulse: {
            distance: 200,
            duration: 0.4
          },
          push: {
            particles_nb: 4
          },
          remove: {
            particles_nb: 2
          }
        }
      },
      retina_detect: true
    });
  }
  
  // Animate weight bars on results page
  const weightBars = document.querySelectorAll('.weight-bar');
  if (weightBars.length > 0) {
    setTimeout(() => {
      weightBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => {
          bar.style.width = width;
        }, 100);
      });
    }, 500);
  }
  
  // Parallax effect for hero section
  const hero = document.querySelector('.hero');
  if (hero) {
    window.addEventListener('scroll', function() {
      const scrollPosition = window.pageYOffset;
      hero.style.backgroundPositionY = scrollPosition * 0.5 + 'px';
    });
  }
  
  // Header scroll effect
  const header = document.querySelector('.glass-header');
  if (header) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        header.style.padding = '0.5rem 2rem';
        header.style.backdropFilter = 'blur(15px)';
      } else {
        header.style.padding = '1rem 2rem';
        header.style.backdropFilter = 'blur(10px)';
      }
    });
  }
});