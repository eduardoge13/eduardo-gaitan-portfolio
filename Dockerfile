FROM nginx:1.30.3-alpine
COPY index.html styles.css script.js /usr/share/nginx/html/
COPY output/pdf/Eduardo_Gaitan_Resume_2026.pdf /usr/share/nginx/html/Eduardo_Gaitan_Resume_2026.pdf
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
