import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { ExamenService } from './examen.service';

describe('ExamenService', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [HttpClientTestingModule], 
    providers: [ExamenService]
  }));

  it('should be created', () => {
    const service: ExamenService = TestBed.inject(ExamenService);
    expect(service).toBeTruthy();
   });

   it('should have getExamen function', () => {
    const service: ExamenService = TestBed.inject(ExamenService);
    expect(service.getExamen).toBeTruthy();
   });
});