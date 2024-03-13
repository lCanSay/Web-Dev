export interface Category {
    id: number;
    name: string;
    image: string;
}

export const categories = [
    {
        id: 1,
        name: "chocolate",
        image: 'https://resources.cdn-kaspi.kz/img/m/p/h21/h90/70365637279774.jpg?format=gallery-medium'
    },
    {
        id: 2,
        name: "beverages",
        image: 'https://resources.cdn-kaspi.kz/img/m/p/h1c/hf1/85128198684702.png?format=gallery-medium',
    },
    {
        id: 3,
        name: "canned",
        image: 'https://kaspi.kz/shop/p/bonduelle-konservirovannye-ovoschi-kukuruza-v-sobstvennom-soku-340-g-100980360/?c=750000000&sr=1&qid=8fd60257404e899ae2148c7747178890&ref=shared_link',
    },
    {
        id: 4,
        name: "vegetables",
        image: 'https://kaspi.kz/shop/p/magnum-perets-sladkii-svetofor-zheltyi-iran-102289200/?c=750000000&sr=23&qid=f916bdd1db1477cbc3bf40b85456d7fc&ref=shared_link',
    }
]