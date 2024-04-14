import {FaShippingFast, FaShieldAlt, FaTags, FaBtc} from 'react-icons/fa';

const servicesData = [
    {
        id: 1,
        icon: <FaShippingFast />,
        title: "Express Delivery",
        info: "Ships in 24 Hours",
    },
    {
        id: 2,
        icon: <FaShieldAlt />,
        title: "Smart Contracts",
        info: "Secure your deals with smart contracts",
    },
    {
        id: 3,
        icon: <FaTags />,
        title: "Exciting Deals",
        info: "On all prepaid orders",
    },
    {
        id: 4,
        icon: <FaBtc />,
        title: "Blockchain Payments",
        info: "Support to various crypto-coins",
    },
];

export default servicesData;