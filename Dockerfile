FROM nginx:1.30.3-alpine
COPY index.html styles.css script.js /usr/share/nginx/html/
COPY assets/atlas-mexico.webp assets/pos-cocina-limpia.webp assets/vivienda-precios.webp assets/tide-demo.webp assets/yoga-verde-producto.webp assets/punto-clave-catalogo.webp /usr/share/nginx/html/assets/
COPY output/pdf/Eduardo_Gaitan_Resume_2026.pdf /usr/share/nginx/html/Eduardo_Gaitan_Resume_2026.pdf
COPY output/pdf/Eduardo_Gaitan_CV_Airtm_AI_Data_Scientist_2026.pdf /usr/share/nginx/html/Eduardo_Gaitan_CV_AI_Data_Scientist_2026.pdf
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
