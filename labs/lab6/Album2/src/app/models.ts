export interface Album {
    id: number;
    title: string;
}

export interface Photo {
    id: number;
    albumId: number;
    title: string;
    url: string;
}