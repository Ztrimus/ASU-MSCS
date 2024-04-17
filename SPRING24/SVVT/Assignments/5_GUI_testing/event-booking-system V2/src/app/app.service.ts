import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor() { }

  events = [
    {
      id: 1,
      title: 'Webinar on Angular',
      description: 'Learn how to create an Angular application in this free Webinar. Learn Angular basics and beyond.',
      image: '',
      date: new Date('2024-04-17T06:30:00'),
      attendees: 9
    },
    {
      id: 2,
      title: 'Workshop on React',
      description: 'Interactive React workshop for beginners.',
      image: '',
      date: new Date('2024-04-17T07:00:00'),
      attendees: 2
    },
    {
      id: 3,
      title: 'Node.js Conference',
      description: 'Join us for the latest trends in Node.js development.',
      image: '',
      date: new Date('2024-04-17T08:00:00'),
      attendees: 35
    },
    {
      id: 4,
      title: 'Python Bootcamp',
      description: 'Intensive Python training for aspiring developers.',
      image: '',
      date: new Date('2024-04-17T09:00:00'),
      attendees: 15
    },
    {
      id: 5,
      title: 'DevOps Summit',
      description: 'Explore best practices in DevOps and automation.',
      image: '',
      date: new Date('2024-04-17T10:00:00'),
      attendees: 50
    },{
      id: 6,
      title: 'Digital Marketing Trends',
      description: 'Explore the future of digital advertising.',
      image: 'https://picsum.photos/id/103/600/400',
      date: new Date('2024-04-18T11:00:00'),
      attendees: 20
    },
    {
      id: 7,
      title: 'Yoga for Beginners',
      description: 'Start your journey with expert guidance.',
      image: 'https://picsum.photos/id/104/600/400',
      date: new Date('2024-04-18T14:00:00'),
      attendees: 15
    },
    {
      id: 8,
      title: 'Sustainable Living Workshop',
      description: 'Practical steps for an eco-friendly lifestyle.',
      image: 'https://picsum.photos/id/105/600/400',
      date: new Date('2024-04-19T16:00:00'),
      attendees: 30
    },
    {
      id: 9,
      title: 'Blockchain Basics',
      description: 'Unlocking the potential of decentralized tech.',
      image: 'https://picsum.photos/id/106/600/400',
      date: new Date('2024-04-20T10:00:00'),
      attendees: 25
    },
    {
      id: 10,
      title: 'AI and Machine Learning Demystified',
      description: 'Understanding AI in today\'s world.',
      image: 'https://picsum.photos/id/107/600/400',
      date: new Date('2024-04-21T09:30:00'),
      attendees: 45
    },
    {
      id: 11,
      title: 'Culinary Arts Experience',
      description: 'Cooking techniques from top chefs.',
      image: 'https://picsum.photos/id/108/600/400',
      date: new Date('2024-04-22T12:00:00'),
      attendees: 12
    },
    {
      id: 12,
      title: 'Jazz Night Live',
      description: 'Experience the magic of live jazz.',
      image: 'https://picsum.photos/id/109/600/400',
      date: new Date('2024-04-23T20:00:00'),
      attendees: 50
    },
  ];
}
