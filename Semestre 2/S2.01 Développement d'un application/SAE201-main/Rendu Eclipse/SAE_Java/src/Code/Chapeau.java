package Code;

import java.util.ArrayList;
import ardoise.*;

public class Chapeau extends Forme {
    private PointPlan point1;
    private PointPlan point2;
    private PointPlan point3;
	
    public Chapeau(Segment seg1, Segment seg2) {
        super("Chapeau");
        this.point1 = seg1.getPointDepart();
        this.point2 = seg1.getPointArrivee();
        this.point3 = seg2.getPointArrivee();
    }

    @Override
    public void deplacer(int Pas_X, int Pas_Y) {
        point1.deplacer(Pas_X, Pas_Y);
        point2.deplacer(Pas_X, Pas_Y);
        point3.deplacer(Pas_X, Pas_Y);
    }

    @Override
    public ArrayList<Segment> dessiner() {
        ArrayList<Segment> segments = new ArrayList<>();
        segments.add(new Segment(point1, point2));
        segments.add(new Segment(point2, point3));
        return segments;
    }

    @Override
    public String typeForme() {
        return "C";
    }
   
}