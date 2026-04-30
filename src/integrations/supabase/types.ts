export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export type Database = {
  // Allows to automatically instantiate createClient with right options
  // instead of createClient<Database, { PostgrestVersion: 'XX' }>(URL, KEY)
  __InternalSupabase: {
    PostgrestVersion: "14.5"
  }
  public: {
    Tables: {
      citations: {
        Row: {
          chunk_id: string | null
          display_order: number | null
          id: string
          query_id: string | null
          relevance_score: number | null
        }
        Insert: {
          chunk_id?: string | null
          display_order?: number | null
          id?: string
          query_id?: string | null
          relevance_score?: number | null
        }
        Update: {
          chunk_id?: string | null
          display_order?: number | null
          id?: string
          query_id?: string | null
          relevance_score?: number | null
        }
        Relationships: [
          {
            foreignKeyName: "citations_chunk_id_fkey"
            columns: ["chunk_id"]
            isOneToOne: false
            referencedRelation: "document_chunks"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "citations_query_id_fkey"
            columns: ["query_id"]
            isOneToOne: false
            referencedRelation: "queries"
            referencedColumns: ["id"]
          },
        ]
      }
      document_chunks: {
        Row: {
          article_reference: string | null
          content: string | null
          embedding: string | null
          id: string
          page_number: number | null
          regulation_id: string | null
        }
        Insert: {
          article_reference?: string | null
          content?: string | null
          embedding?: string | null
          id?: string
          page_number?: number | null
          regulation_id?: string | null
        }
        Update: {
          article_reference?: string | null
          content?: string | null
          embedding?: string | null
          id?: string
          page_number?: number | null
          regulation_id?: string | null
        }
        Relationships: [
          {
            foreignKeyName: "document_chunks_regulation_id_fkey"
            columns: ["regulation_id"]
            isOneToOne: false
            referencedRelation: "regulations"
            referencedColumns: ["id"]
          },
        ]
      }
      queries: {
        Row: {
          answer: string | null
          confidence_score: number | null
          created_at: string
          flagged_for_review: boolean
          id: string
          question: string
          user_id: string | null
        }
        Insert: {
          answer?: string | null
          confidence_score?: number | null
          created_at?: string
          flagged_for_review?: boolean
          id?: string
          question: string
          user_id?: string | null
        }
        Update: {
          answer?: string | null
          confidence_score?: number | null
          created_at?: string
          flagged_for_review?: boolean
          id?: string
          question?: string
          user_id?: string | null
        }
        Relationships: [
          {
            foreignKeyName: "queries_user_id_fkey"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "users"
            referencedColumns: ["id"]
          },
        ]
      }
      regulations: {
        Row: {
          chunks_indexed: number | null
          id: string
          jurisdiction: string | null
          last_synced: string | null
          name: string
          pages: number | null
          status: string | null
          version: string | null
        }
        Insert: {
          chunks_indexed?: number | null
          id?: string
          jurisdiction?: string | null
          last_synced?: string | null
          name: string
          pages?: number | null
          status?: string | null
          version?: string | null
        }
        Update: {
          chunks_indexed?: number | null
          id?: string
          jurisdiction?: string | null
          last_synced?: string | null
          name?: string
          pages?: number | null
          status?: string | null
          version?: string | null
        }
        Relationships: []
      }
      reviewer_actions: {
        Row: {
          action: string
          created_at: string
          id: string
          notes: string | null
          query_id: string | null
          reviewer_id: string | null
        }
        Insert: {
          action: string
          created_at?: string
          id?: string
          notes?: string | null
          query_id?: string | null
          reviewer_id?: string | null
        }
        Update: {
          action?: string
          created_at?: string
          id?: string
          notes?: string | null
          query_id?: string | null
          reviewer_id?: string | null
        }
        Relationships: [
          {
            foreignKeyName: "reviewer_actions_query_id_fkey"
            columns: ["query_id"]
            isOneToOne: false
            referencedRelation: "queries"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "reviewer_actions_reviewer_id_fkey"
            columns: ["reviewer_id"]
            isOneToOne: false
            referencedRelation: "users"
            referencedColumns: ["id"]
          },
        ]
      }
      users: {
        Row: {
          email: string
          id: string
          name: string
          role: string
        }
        Insert: {
          email: string
          id?: string
          name: string
          role: string
        }
        Update: {
          email?: string
          id?: string
          name?: string
          role?: string
        }
        Relationships: []
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      match_document_chunks:
        | {
            Args: { match_count?: number; query_embedding: string }
            Returns: {
              article_reference: string
              content: string
              id: string
              page_number: number
              regulation_id: string
              regulation_name: string
              similarity: number
            }[]
          }
        | {
            Args: {
              filter_regulation_id?: string
              match_count?: number
              query_embedding: string
            }
            Returns: {
              article_reference: string
              content: string
              id: string
              page_number: number
              regulation_id: string
              regulation_name: string
              similarity: number
            }[]
          }
    }
    Enums: {
      [_ in never]: never
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}

type DatabaseWithoutInternals = Omit<Database, "__InternalSupabase">

type DefaultSchema = DatabaseWithoutInternals[Extract<keyof Database, "public">]

export type Tables<
  DefaultSchemaTableNameOrOptions extends
    | keyof (DefaultSchema["Tables"] & DefaultSchema["Views"])
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
        DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
      DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])[TableName] extends {
      Row: infer R
    }
    ? R
    : never
  : DefaultSchemaTableNameOrOptions extends keyof (DefaultSchema["Tables"] &
        DefaultSchema["Views"])
    ? (DefaultSchema["Tables"] &
        DefaultSchema["Views"])[DefaultSchemaTableNameOrOptions] extends {
        Row: infer R
      }
      ? R
      : never
    : never

export type TablesInsert<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Insert: infer I
    }
    ? I
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
    ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
        Insert: infer I
      }
      ? I
      : never
    : never

export type TablesUpdate<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Update: infer U
    }
    ? U
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
    ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
        Update: infer U
      }
      ? U
      : never
    : never

export type Enums<
  DefaultSchemaEnumNameOrOptions extends
    | keyof DefaultSchema["Enums"]
    | { schema: keyof DatabaseWithoutInternals },
  EnumName extends DefaultSchemaEnumNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"]
    : never = never,
> = DefaultSchemaEnumNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"][EnumName]
  : DefaultSchemaEnumNameOrOptions extends keyof DefaultSchema["Enums"]
    ? DefaultSchema["Enums"][DefaultSchemaEnumNameOrOptions]
    : never

export type CompositeTypes<
  PublicCompositeTypeNameOrOptions extends
    | keyof DefaultSchema["CompositeTypes"]
    | { schema: keyof DatabaseWithoutInternals },
  CompositeTypeName extends PublicCompositeTypeNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"]
    : never = never,
> = PublicCompositeTypeNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"][CompositeTypeName]
  : PublicCompositeTypeNameOrOptions extends keyof DefaultSchema["CompositeTypes"]
    ? DefaultSchema["CompositeTypes"][PublicCompositeTypeNameOrOptions]
    : never

export const Constants = {
  public: {
    Enums: {},
  },
} as const
