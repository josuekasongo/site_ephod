# -*- coding: utf-8 -*-
import codecs

filename = r'd:\\EPHOD\\js\\lang.js'

content = """const translations = {
    fr: {
        "nav.home": "Accueil",
        "nav.about": "Qui sommes-nous ?",
        "nav.services": "Nos services",
        "nav.portfolio": "Nos réalisations",
        "nav.ongoing": "En cours de réalisation",
        "nav.careers": "Offres d'emploi",
        "nav.logo": "EPHOD Consulting",
        
        "nav.drop_vision": "Notre Vision",
        "nav.drop_vision_sub": "Identité & Valeurs",
        "nav.drop_team": "Notre Équipe",
        "nav.drop_team_sub": "Nos experts dédiés",
        "nav.drop_strat_short": "Stratégie",
        "nav.drop_strat_sub2": "Advisory & Conseil",
        "nav.drop_digital_short": "Digital",
        "nav.drop_digital_sub2": "Transformation IT",
        "nav.drop_public_short": "Études & Évaluations",
        "nav.drop_public_sub2": "Consulting Expert",
        
        "nav.drop_strat": "Stratégie",
        "nav.drop_strat_sub": "Projets d'Entreprise",
        "nav.drop_digi": "Digital",
        "nav.drop_digi_sub": "Transformation Numérique",
        "nav.drop_pub": "Public",
        "nav.drop_pub_sub": "Secteur Public",
        "nav.drop_ongoing_now": "Chantiers Actuels",
        "nav.drop_ongoing_now_sub": "Déploiements en cours",
        "nav.drop_ongoing_long": "Missions Long Terme",
        "nav.drop_ongoing_long_sub": "Progression & Impact",
        "nav.drop_careers_open": "Postes Ouverts",
        "nav.drop_careers_open_sub": "Rejoignez l'excellence",
        "nav.drop_careers_apply": "Candidature",
        "nav.drop_careers_apply_sub": "Spontanée",

        "hero.eyebrow": "CONSEIL • INNOVATION • IMPACT",
        "hero.line1": "L'Expertise Institutionnelle",
        "hero.line2": "au Service de vos Ambitions.",
        "hero.subtitle": "Cabinet de conseil engagé pour renforcer les conditions d'un développement économique et social durable en Afrique.",
        "hero.btn_discover": "Nos Domaines",
        "hero.btn_about": "Notre Mission",

        "home.services_label": "NOTRE OFFRE",
        "home.services_title": "Une expertise <span>contextualisée</span>",
        "home.about_title": "Cabinet d'Expertises <span style='color: var(--primary); font-weight: 900;'>Stratégiques</span> et Opérationnelles",
        "home.about_desc": "EPHOD Consulting allie rigueur analytique et innovation pour transformer vos organisations face aux défis complexes du terrain.",
        "home.news_title": "DERNIÈRES ACTUALITÉS",
        "home.news_btn": "Tout voir",

        "services.banner_title": "Nos Domaines d'Expertise",
        "services.banner_sub": "L'ingénierie stratégique au service de l'excellence : nous concevons des solutions sur mesure alliant rigueur analytique et innovation pour transformer vos défis complexes en leviers de croissance durable.",
        "services.expertise_label": "Notre approche",
        "services.expertise_title": "Une expertise <span>pluridisciplinaire</span> à votre service",
        "services.expertise_desc": "Chaque organisation est unique. Nos interventions sont toujours contextualisées, co-construites avec vos équipes, et orientées vers des résultats mesurables et durables.",

        "srv.s1_title": "CONSULTING & INGÉNIERIE ANALYTIQUE",
        "srv.s1_desc": "Expertise analytique de pointe tout au long du cycle de projet. De la Baseline aux évaluations d'impact finales, nous transformons les données en leviers d'action concrets et mesurables pour vos programmes.",
        "srv.s2_desc": "Accompagnement de haut niveau pour les directions générales et investisseurs. Nous sécurisons vos prises de décision par des analyses prospectives et des feuilles de route opérationnelles agiles.",
        "srv.s3_desc": "Concevoir des solutions robustes pour la mobilisation de ressources internationales. Nous structurons des projets répondant aux standards les plus exigeants des bailleurs de fonds mondiaux.",
        "srv.s4_desc": "Programmes de renforcement tactique et stratégique pour les cadres des institutions et du secteur humanitaire. Des formations certifiantes axées sur l'excellence opérationnelle et le leadership.",
        "srv.s5_desc": "Pionniers dans le déploiement de solutions de transfert monétaire sécurisé. Nous facilitons les interventions Cash et Mobile Money, assurant une inclusion financière même dans les zones les plus complexes.",
        "srv.s6_desc": "Le numérique au service de l'impact. Nous déployons des Systèmes d'Information Géographique (SIG) et des outils de collecte mobile pour une visualisation et une analyse en temps réel de vos données stratégiques.",
        "srv.s7_desc": "Audit global de l'efficacité organisationnelle. Nous optimisons votre gouvernance et vos processus internes pour maximiser l'impact de vos interventions tout en réduisant les coûts opérationnels.",

        "footer.desc": "Cabinet de conseil expert en stratégie, innovation et transformation.",
        "footer.nav_title": "Navigation",
        "footer.services_title": "Services",
        "footer.contact_title": "Contact",
        "footer.address": "123 Avenue de la République, Kinshasa, RDC",
        "footer.rights": "Tous droits réservés.",
        "footer.made": "EPHOD CONSULTING SARL",
        
        "cta.title": "Prêt à transformer votre vision ?",
        "cta.sub": "Discutons de votre projet dès aujourd'hui.",
        "cta.btn": "Prendre contact",

        "about.rccm": "RCCM : CD/KNG/RCCM/25-B-03958",
        "about.idnat": "ID NAT : 01-H5300-N88322C",
        "about.ungm": "UNGM : 1175536",
        "about.nif": "Impôt : A2559012X",
        "about.inpp": "N° INPP : 166976,00",
        
        "port.cat1": "Conseil Stratégique",
        "port.cat2": "Digital & Transformation",
        "port.cat3": "Secteur Public & ONG",
        "port.p1_title": "Audit de Gouvernance",
        "port.p2_title": "Transformation Numérique",
        "port.p3_title": "Études d'Impact",
        "port.more": "En savoir plus"
    },
    en: {
        "nav.home": "Home",
        "nav.about": "About Us",
        "nav.services": "Services",
        "nav.portfolio": "Our Works",
        "nav.ongoing": "Ongoing Projects",
        "nav.careers": "Careers",
        "nav.logo": "EPHOD Consulting",
        
        "nav.drop_vision": "Our Vision",
        "nav.drop_vision_sub": "Identity & Values",
        "nav.drop_team": "Our Team",
        "nav.drop_team_sub": "Our dedicated experts",
        
        "hero.eyebrow": "CONSULTING • INNOVATION • IMPACT",
        "hero.line1": "Institutional Expertise",
        "hero.line2": "at the Service of Your Ambitions.",
        "hero.subtitle": "A consulting firm committed to strengthening the conditions for sustainable economic and social development in Africa.",
        
        "services.banner_title": "Our Areas of Expertise",
        "services.banner_sub": "Strategic engineering at the service of excellence: we design tailored solutions combining analytical rigor and innovation to transform your complex challenges into drivers of sustainable growth.",
        "services.expertise_label": "Our approach",
        "services.expertise_title": "A <span>multidisciplinary</span> expertise at your service",
        
        "srv.s1_title": "CONSULTING & ANALYTICAL ENGINEERING",
        "srv.s1_desc": "Leading analytical expertise throughout the project cycle. From Baseline studies to final impact assessments, we transform data into concrete and measurable action for your programs.",
        "srv.s2_title": "ADVISORY & GOVERNANCE",
        "srv.s2_desc": "High-level support for general management and investors. We secure your decision-making through prospective analyses and agile operational roadmaps.",
        "srv.s3_title": "ENGINEERING & MOBILIZATION",
        "srv.s3_desc": "Design robust solutions for the mobilization of international resources. We structure projects meeting the most demanding standards of global donors.",
        "srv.s4_title": "CAPACITY BUILDING & ELITE TRAINING",
        "srv.s4_desc": "Tactical and strategic strengthening programs for institutional and humanitarian staff. Certifying training focused on operational excellence and leadership.",
        "srv.s5_title": "MONETARY & CASH ENGINEERING",
        "srv.s5_desc": "Pioneers in deploying secure monetary transfer solutions. We facilitate Cash and Mobile Money interventions, ensuring financial inclusion even in the most complex areas.",
        "srv.s6_title": "DIGITAL INTELLIGENCE & GIS",
        "srv.s6_desc": "Technology at the service of impact. We deploy Geographic Information Systems (GIS) and mobile collection tools for real-time visualization and analysis of your strategic data.",
        "srv.s7_title": "AUDIT & PERFORMANCE",
        "srv.s7_desc": "Global audit of organizational efficiency. We optimize your governance and internal processes to maximize the impact of your interventions while reducing operational costs.",
        
        "footer.contact_title": "Contact",
        "footer.rights": "All rights reserved.",
        "footer.made": "EPHOD CONSULTING SARL",
        
        "cta.title": "Ready to transform your vision?",
        "cta.sub": "Let's discuss your project today.",
        "cta.btn": "Contact Us"
    }
};

let currentLang = localStorage.getItem('ephod_lang') || 'fr';

function toggleLanguage() {
    currentLang = currentLang === 'fr' ? 'en' : 'fr';
    localStorage.setItem('ephod_lang', currentLang);
    updateLangUI();
    applyTranslations();
    
    // If we're on a page with hero animation, restart it
    if (window.resetHeroAnimation) {
        window.stopAllTypewriters();
        window.resetHeroAnimation();
    }
}

function updateLangUI() {
    const langBtn = document.getElementById('lang-toggle-text');
    if (langBtn) langBtn.innerText = currentLang.toUpperCase();
}

function applyTranslations() {
    const elements = document.querySelectorAll('[data-i18n]');
    elements.forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[currentLang] && translations[currentLang][key]) {
            const val = translations[currentLang][key];
            
            // Special handling for typewriter attributes
            if (el.hasAttribute('data-text')) {
                el.setAttribute('data-text', val);
            }
            if (el.hasAttribute('data-html')) {
                el.setAttribute('data-html', val);
            }
            
            // Apply innerHTML if NOT currently typing or if it's a static element
            if (!el.classList.contains('typing-active')) {
                el.innerHTML = val;
            }
        }
    });

    const placeholders = document.querySelectorAll('[data-i18n-placeholder]');
    placeholders.forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[currentLang] && translations[currentLang][key]) {
            el.placeholder = translations[currentLang][key];
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    updateLangUI();
    applyTranslations();
});
"""

with codecs.open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Success: lang.js rebuilt with extended translations and attribute handling.")
